import os

class sceneRenderer:
    def __init__(self):
        # os.system('cls')
        self.__saveScene = {}
        self.__currentScene = ''
    
    def setScenes(self, scene: dict):
        if 'name' in scene and 'desc' in scene and 'options' in scene:
            self.__saveScene[scene['name']] = scene
            self.showAllScenes()
        else:
            raise Exception("You don't have the correct format for scene. You need have 'name', 'desc' and 'options' key in your dictionary.")

    def createBasicScene(self, name: str, description: str, options: list):
        return {'name': name, 'desc': description, 'options': options}

    def getAllScenes(self):
        return self.__saveScene
    
    def getSceneInfo(self, sceneName: str):
        return self.__saveScene[sceneName]
    
    def setCurrentScene(self, currentSceneName: str):
        self.__currentScene = currentSceneName
    
    def getCurrentScene(self):
        return self.__currentScened

    def transportToScene(self, targetSceneName: str):
        self.__currentScene = targetSceneName

    def showAllScenes(self):
        print('scene name|\tscene description')
        for scene in self.__saveScene:
            print(f"{self.__saveScene[scene]['name']}|\t{self.__saveScene[scene]['desc']}")

    def showSceneInfo(self, sceneName: str):
        scene = self.__saveScene[sceneName]
        sceneKey = list(scene.keys())
        for sk in sceneKey:
            print(f"{sk}: {scene[sk]}")
                
    def sceneCommad(self, sceneName: str, commandName: str, commandContent: str):
        if sceneName in self.__saveScene and commandName not in self.__saveScene[sceneName]:
            self.__saveScene[sceneName][commandName] = commandContent
        else:
            raise Exception("Your scenes not include the scene name or other scene name")
    
    def getSceneCommand(self, sceneName: str, commandName: str):
        if sceneName in self.__saveScene and commandName in self.__saveScene[sceneName]:
            return self.__saveScene[sceneName][commandName]
        else:
            raise Exception('The scene name or command name not found..')

    def renderScene(self, sceneChoice: str = '', optionChoice: int = 0, useInnerCurrentScene: bool = False):
        if useInnerCurrentScene:
            sceneDesc = self.__currentScene
        elif sceneChoice != '':
            sceneDesc = self.__saveScene[sceneChoice]['desc']
        else:
            raise Exception("The parameter 'sceneChoice' need input something.")
        options = self.__saveScene[sceneChoice]['options']
        options[optionChoice] = '> ' + options[optionChoice]
        os.system('cls')
        optionsStr = '\n'.join(options)
        print(f"description:\n{sceneDesc}\n\n{optionsStr}")