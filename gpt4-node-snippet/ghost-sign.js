
var request = require ("request");
var crypto = require ("crypto");

module.exports = function(){

    this.id = "my-first-action"; 

    this.label = "Sample"; 

    this.help = "Sample code for reference"; 

    this.input = {
        "title": "Test Secret",
        "type": "object",
        "properties": {
            "webhook_secret": {
                "title": "WebHook Secret",// displayed as field label  
                "type": "string",
                "format": "password",
                "description":"Enter the same value, used for ˝host webhook.",// description of field
                "minLength": 1 // define as required
            },
            "webhook_signature": {
                "title": "WebHook Signature",// displayed as field label  
                "type": "string",
                "description":"Value of the X-Ghost-Signature header",// description of field
                "minLength": 1 // define as required
            },
            "webhook_body": {
                "title": "WebHook Request",// displayed as field label  
                "type": "any",
                "format": "textarea",
                "description":"The body of the request",// description of field
                "minLength": 1 // define as required
            }
        }
    }; 

    this.output = {
        "title" : "output",
        "type" : "object",
        "properties":{
            "status":{
                "title":"status",
                "type" :"string"
            }
        }
    }; 


    this.execute = function(input,output){
        
        // `ha256=${crypto.createHmac('sha256', secret).update(`${reqPayload}${ts}`).digest('hex')}, t=${ts}`;
        parsedSignature = {};
        input.webhook_signature.split(",")
         .forEach(part => {
             const [key,value] = part.trim().split("=");
             parsedSignature[key]=value  ;
         });
        $log(`Parsed header : ${parsedSignature}`);
        
        myHash=crypto.createHmac("sha256", input.webhook_secret).update(`${input.webhook_body}${parsedSignature.t}`).digest("hex");
        $log(`Calculated hash: ${myHash}`);
        
        if( parsedSignature.ha256 === myHash )
            return output(null,{ "status":"Signature is valid!"});
        else
            return output({ "error": `Signature ${parsedSignature.sha256} doesn't match ${myHash}`},null);
        
    }
};
