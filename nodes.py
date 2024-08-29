import comfy.sd


class WidthHeightMittimi01:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
                    "Width": ("INT", {"default": 512, "min": 1, "max": 2147483647} ),
                    "Height": ("INT", {"default": 512, "min": 1, "max": 2147483647} ),
                },
                "hidden": {"node_id": "UNIQUE_ID" }
        }

    RETURN_TYPES = ("INT", "INT", )
    RETURN_NAMES = ("width", "height", )
    FUNCTION = "runWidthHeight"
    CATEGORY = "mittimiTools"

    def runWidthHeight(self, Width, Height, node_id, ):        
        return(Width, Height, )


NODE_CLASS_MAPPINGS = {
    "WidthHeightMittimi01": WidthHeightMittimi01,   
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "WidthHeightMittimi01": "WidthHeight01", 
}
