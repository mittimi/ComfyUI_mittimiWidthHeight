import comfy.sd
import toml
import os
import re


my_directory_path = os.path.dirname((os.path.abspath(__file__)))
presets__path = os.path.join(my_directory_path, "presets/presets.toml")
preset_data = ""
with open(presets__path, 'r') as f:
    preset_data = toml.load(f)
wh_list =  re.findall(r"\b\d+x\d+\b", preset_data['wh'])


class WidthHeightMittimi01:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
                    "Width": ("INT", {"default": 512, "min": 1, "max": 2147483647} ),
                    "Height": ("INT", {"default": 512, "min": 1, "max": 2147483647} ),
                },
                "optional": {
                    "preset": (wh_list, ),
                },
                "hidden": {"node_id": "UNIQUE_ID" }
        }

    RETURN_TYPES = ("INT", "INT", )
    RETURN_NAMES = ("width", "height", )
    FUNCTION = "runWidthHeight"
    CATEGORY = "mittimiTools"

    def runWidthHeight(self, Width, Height, node_id, preset=[], ):        
        return(Width, Height, )


NODE_CLASS_MAPPINGS = {
    "WidthHeightMittimi01": WidthHeightMittimi01,   
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "WidthHeightMittimi01": "WidthHeight01", 
}
