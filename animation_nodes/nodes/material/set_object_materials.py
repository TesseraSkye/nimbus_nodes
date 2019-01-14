import bpy
from ... base_types import AnimationNode, VectorizedSocket

class SetObjectMaterialsNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_SetObjectMaterialsNode"
    bl_label = "Set Object Materials"

    useList: VectorizedSocket.newProperty()

    def create(self):
        self.newInput("Object", "Object", "object", defaultDrawType = "PROPERTY_ONLY")
        self.newInput(VectorizedSocket("Material", "useList",
            ("Material", "material"),
            ("Materials", "materials")), defaultDrawType = "PROPERTY_ONLY")

        self.newOutput("Object", "Object", "object")

    def getExecutionFunctionName(self):
        if self.useList:
            return "executeList"
        else:
            return "executeSingle"

    def executeSingle(self, object, material):
        if object == None or not hasattr(object.data, "materials"): return object
        object.data.materials.clear()
        object.data.materials.append(material)
        return object

    def executeList(self, object, materials):
        if object == None or not hasattr(object.data, "materials"): return object
        object.data.materials.clear()
        for material in materials:
            object.data.materials.append(material)
        return object