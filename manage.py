from psd_tools import PSDImage
import os
import json


def make_scene(psdPath, resDirPath):
    psdDirPath, psdFileName = os.path.split(psdPath)
    mapName = os.path.splitext(psdFileName)[0]
    mapDirPath = os.path.join(resDirPath, mapName)
    imageDirPath = os.path.join(mapDirPath, 'images')
    sceneFilePath = os.path.join(mapDirPath, 'scene.json')

    if not os.access(imageDirPath, os.R_OK):
        os.makedirs(imageDirPath)

    psd = PSDImage.load(psdPath)

    layerInfos = []
    for layer in psd.layers:
        if layer.name == 'num':
            continue

        layerInfo = dict(
            name=layer.name.encode('utf8'),
            x=layer.bbox.x1,
            y=psd.header.height - layer.bbox.y2,
            w=layer.bbox.width,
            h=layer.bbox.height)

        layerInfos.append(layerInfo)

        if True:
            image = layer.as_PIL()
            image.save('{0}/{1}.png'.format(imageDirPath, layer.name))

    sceneDict = dict(layers=layerInfos, header=dict(width=psd.header.width, height=psd.header.height))
    open(sceneFilePath, 'w').write(json.dumps(sceneDict, indent=4))

make_scene('./graphics/maps/china.psd', './resources/maps')
