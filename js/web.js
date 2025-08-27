import { ComfyApp, app } from "../../scripts/app.js";


var allow_set_flag = true;


app.registerExtension({
	name: "ComfyUI_mittimiWidthHeight",


    async beforeConfigureGraph() {
        allow_set_flag = false;
    },


    async nodeCreated(node) {        

        if (node.comfyClass == "WidthHeightMittimi01") {

            Object.defineProperty(node.widgets[2], "value", {

                set: (value) => {

                    node._value = value;

                    
                    if (allow_set_flag) {
                        var splitvalue = value.split("x");
                        node.widgets[0].value = parseInt( splitvalue[0] );
                        node.widgets[1].value = parseInt( splitvalue[1] );
                    }
                    
                },

                get: () => {
                    return node._value;
                }
                
            });

            node.addWidget("button", "Swap", "value maybe?", (...args) => {
                
                var wv = node.widgets[0].value;
                node.widgets[0].value = node.widgets[1].value;
                node.widgets[1].value = wv;
            })
        }
    }, 


    async afterConfigureGraph() {
        allow_set_flag = true;
    }
});
