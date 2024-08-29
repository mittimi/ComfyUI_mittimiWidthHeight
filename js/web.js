import { ComfyApp, app } from "../../scripts/app.js";


app.registerExtension({
	name: "ComfyUI_mittimiWidthHeight",

    async nodeCreated(node) {
        if (node.comfyClass == "WidthHeightMittimi01") {

            node.addWidget("button", "Swap", "value maybe?", (...args) => {
                
                var wv = node.widgets[0].value;
                node.widgets[0].value = node.widgets[1].value;
                node.widgets[1].value = wv;
            })
        }
    }
});



    