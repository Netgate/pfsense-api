// Example pfSense API JavaScript client
//
// Prep:
//    Generate the JavaScript library using:
//
//    $ openapi-generator-cli generate -g javascript -o js -i pfapi_openapi.yml
//
//    Modify the generated JavaScript library's package.json with the
//    path of the built sources so that this script can import it, for example:
//
//    "exports": {
//        ".": "./dist/index.js"
//    },
//
// To run: copy this script to the js directory and run with node
//    PASSWORD=secret node example.js
//

const API = require('pf_sense_api');

// To be able to use with self-signed Controller TLS certificates:
process.env["NODE_TLS_REJECT_UNAUTHORIZED"] = 0;

let USERNAME = process.env["USERNAME"] || "admin";
let PASSWORD = process.env["PASSWORD"];

// Change this to your Controller's address
let CONTROLLER_URL = "https://10.100.0.38:8443";

function newClient(subpath) {
    let basePath = CONTROLLER_URL + '/api';
    if (subpath) {
       basePath += '/' + subpath;
    }

    const client = new API.ApiClient();
    client.basePath = basePath;

    client.setBearer = function(tok) {
        if (tok) {
            let v = Object();
            v.type = "bearer";
            v.accessToken = tok;
            this.authentications["bearer"] = v;
        }
    }
    client.getBearer = function() {
        try {
            return this.authentications["bearer"].accessToken;
        } catch (error) {
            return null;
        }
    }
    customizeClient(client);

    return client;
}

// Adjust OpenAPI generated client with a call wrapper which
// inserts the required "Authorization: bearer" header into
// the requests
function customizeClient(client) {
    client._callApi = client.callApi;

    // Override callApi so that we can inject our own authParams
    client.callApi = function(path, httpMethod, pathParams,
        queryParams, headerParams, formParams, bodyParam, authNames, contentTypes, accepts,
        returnType, apiBasePath, callback) {

        if (Object.keys(this.authentications).length > 0)
            authNames = ["bearer"];

        return this._callApi(path, httpMethod, pathParams,
            queryParams, headerParams, formParams, bodyParam, authNames, contentTypes, accepts,
            returnType, apiBasePath, callback);
    }
}


function listDevices(client) {
    const mim = new API.MimApi(client);

    mim.getControlledDevices(null, function(error, data, response) {
        if (error) {
            console.error(error);
        } else {
            //
            // For each device, get their system information via MIM
            //
            data.devices.forEach(function(device) {
                console.log("Querying device: " + device.device_id);

                let devClient = newClient("device/pfsense/" + device.device_id + "/api");
                devClient.setBearer(client.getBearer());

                var interfaces = new API.InterfacesApi(devClient);
                interfaces.getInterfaces(function(error, result, response) {
                    if  (error) {
                        console.log("ERROR: Get device " + device.device_id + " interfaces failed: " + error);
                    } else {
                        console.log("=========== " + device.name + " " + device.device_id + "=========");
                        result.interfaces.forEach(function(intf) {
                            console.log("Name:", intf.name, "/ Assigned:", intf.descr, "/ Device:", intf.if,
                                   "/ MAC:", intf.mac, "/ IP:", intf.ipaddr);
                        })
                    }
                })
            })
        }
    });
}


//
// Create base client, perform login to get the authorization token, and
// call listDevices() to perform some action on each device.
//

let apiClient = newClient();
const login = new API.LoginApi(apiClient);
var loginReq = new API.LoginCredentials(btoa(USERNAME), btoa(PASSWORD));
var callback = function(error, data, response) {
    if (error) {
        console.error(error);
    } else {
        console.log('Login successful: ' + JSON.stringify(data, "", "  "));
        apiClient.setBearer(data.token);

        listDevices(apiClient);
    }
};
login.login(loginReq, callback);
