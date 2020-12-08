#!/usr/bin/env python
# -- coding: utf-8 --
# author: morgan time:2020/12/7
import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from ui_mainwindow import Ui_Form
from Demo import *


class MainWindow(QMainWindow):
    global camera, streamSource, userInfo, cameraList, trigModeEnumNode

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def enum_devices_clicked(self):
        print('enum_devices_clicked')
        # self.ui.line_device_number.setText("dahua1")
        # self.ui.combo_device_list.addItem('dahua120')

        # 发现相机
        # enumerate camera
        cameraCnt, cameraList = enumCameras()
        if cameraCnt is None:
            return -1

        # 显示相机信息
        # print camera info
        for index in range(0, cameraCnt):
            camera = cameraList[index]
            print("\nCamera Id = " + str(index))
            print("Key           = " + str(camera.getKey(camera)))
            print("vendor name   = " + str(camera.getVendorName(camera)))
            print("Model  name   = " + str(camera.getModelName(camera)))
            print("Serial number = " + str(camera.getSerialNumber(camera)))

            self.ui.combo_device_list.addItem(str(camera.getModelName(camera)))

        self.ui.line_device_number.setText(cameraCnt)

        camera = cameraList[0]

    def device_list_changed(self):
        camera = cameraList[self.ui.combo_device_list.currentIndex()]
        pass

    def open_device_clicked(self):
        # 打开相机
        # open camera
        nRet = openCamera(camera)
        if nRet != 0:
            print("openCamera fail.")
            return -1

        # 创建流对象
        # create stream source object
        streamSourceInfo = GENICAM_StreamSourceInfo()
        streamSourceInfo.channelId = 0
        streamSourceInfo.pCamera = pointer(camera)

        streamSource = pointer(GENICAM_StreamSource())
        nRet = GENICAM_createStreamSource(pointer(streamSourceInfo), byref(streamSource))
        if nRet != 0:
            print("create StreamSource fail!")
            return -1
        # 通用属性设置:设置触发模式为off --根据属性类型，直接构造属性节点。如触发模式是 enumNode，构造enumNode节点
        # create corresponding property node according to the value type of property, here is enumNode
        # 自由拉流：TriggerMode 需为 off
        # set trigger mode to Off for continuously grabbing
        trigModeEnumNode = pointer(GENICAM_EnumNode())
        trigModeEnumNodeInfo = GENICAM_EnumNodeInfo()
        trigModeEnumNodeInfo.pCamera = pointer(camera)
        trigModeEnumNodeInfo.attrName = b"TriggerMode"
        nRet = GENICAM_createEnumNode(byref(trigModeEnumNodeInfo), byref(trigModeEnumNode))
        if nRet != 0:
            print("create TriggerMode Node fail!")
            # 释放相关资源
            # release node resource before return
            streamSource.contents.release(streamSource)
            return -1

        nRet = trigModeEnumNode.contents.setValueBySymbol(trigModeEnumNode, b"Off")
        if nRet != 0:
            print("set TriggerMode value [Off] fail!")
            # 释放相关资源
            # release node resource before return
            trigModeEnumNode.contents.release(trigModeEnumNode)
            streamSource.contents.release(streamSource)
            return -1

        # 需要释放Node资源
        # release node resource at the end of use
        trigModeEnumNode.contents.release(trigModeEnumNode)

        pass

    def close_device_clicked(self):
        # 关闭相机
        # close camera
        nRet = closeCamera(camera)
        if nRet != 0:
            print("closeCamera fail")
            # 释放相关资源
            # release stream source object before return
            streamSource.contents.release(streamSource)
            return -1

        # 释放相关资源
        # release stream source object at the end of use
        streamSource.contents.release(streamSource)
        pass

    def radio_continuous_clicked(self):
        if self.ui.radio_continuous.isChecked():
            nRet = trigModeEnumNode.contents.setValueBySymbol(trigModeEnumNode, b"Off")
            if nRet != 0:
                print("set TriggerMode value [Off] fail!")
                # 释放相关资源
                # release node resource before return
                trigModeEnumNode.contents.release(trigModeEnumNode)
                streamSource.contents.release(streamSource)
                return -1
        else:
            nRet = trigModeEnumNode.contents.setValueBySymbol(trigModeEnumNode, b"on")
            if nRet != 0:
                print("set TriggerMode value [on] fail!")
                # 释放相关资源
                # release node resource before return
                trigModeEnumNode.contents.release(trigModeEnumNode)
                streamSource.contents.release(streamSource)
                return -1
        pass

    def radio_trigger_clicked(self):
        if self.ui.radio_trigger.isChecked():
            nRet = trigModeEnumNode.contents.setValueBySymbol(trigModeEnumNode, b"on")
            if nRet != 0:
                print("set TriggerMode value [on] fail!")
                # 释放相关资源
                # release node resource before return
                trigModeEnumNode.contents.release(trigModeEnumNode)
                streamSource.contents.release(streamSource)
                return -1
        else:
            nRet = trigModeEnumNode.contents.setValueBySymbol(trigModeEnumNode, b"Off")
            if nRet != 0:
                print("set TriggerMode value [Off] fail!")
                # 释放相关资源
                # release node resource before return
                trigModeEnumNode.contents.release(trigModeEnumNode)
                streamSource.contents.release(streamSource)
                return -1
        pass

    def start_grabbing_clicked(self):
        # 注册拉流回调函数
        # subscribe grabbing callback
        userInfo = b"test"
        nRet = streamSource.contents.attachGrabbingEx(streamSource, frameCallbackFuncEx, userInfo)
        if nRet != 0:
            print("attachGrabbingEx fail!")
            # 释放相关资源
            # release stream source object before return
            streamSource.contents.release(streamSource)
            return -1

        # 开始拉流
        # start grabbing
        nRet = streamSource.contents.startGrabbing(streamSource, c_ulonglong(0),
                                                   c_int(GENICAM_EGrabStrategy.grabStrartegySequential))
        if nRet != 0:
            print("startGrabbing fail!")
            # 释放相关资源
            # release stream source object before return
            streamSource.contents.release(streamSource)
            return -1

        pass

    def stop_grabbing_clicked(self):
        # 反注册回调函数
        # unsubscribe grabbing callback
        nRet = streamSource.contents.detachGrabbingEx(streamSource, frameCallbackFuncEx, userInfo)
        if nRet != 0:
            print("detachGrabbingEx fail!")
            # 释放相关资源
            # release stream source object before return
            streamSource.contents.release(streamSource)
            return -1
        # 停止拉流
        # stop grabbing
        nRet = streamSource.contents.stopGrabbing(streamSource)
        if nRet != 0:
            print("stopGrabbing fail!")
            # 释放相关资源
            # release stream source object before return
            streamSource.contents.release(streamSource)
            return -1

        pass

    def trigger_software_clicked(self):
        if (self.ui.checkbtn_trigger_software.isChecked):
            # 设置软触发
            # set software trigger config
            nRet = setSoftTriggerConf(camera)
            if nRet != 0:
                print("set SoftTriggerConf fail!")
                # 释放相关资源
                # release stream source object before return
                streamSource.contents.release(streamSource)
                return -1
            else:
                print("set SoftTriggerConf success!")
        else:
            # 停止拉流
            # stop grabbing
            nRet = streamSource.contents.stopGrabbing(streamSource)
            if nRet != 0:
                print("stopGrabbing fail!")
                # 释放相关资源
                # release stream source object before return
                streamSource.contents.release(streamSource)
                return -1
        pass

    def trigger_once_clicked(self):
        # 开始拉流
        # start grabbing
        nRet = streamSource.contents.startGrabbing(streamSource, c_ulonglong(0), \
                                                   c_int(GENICAM_EGrabStrategy.grabStrartegySequential))
        if nRet != 0:
            print("startGrabbing fail!")
            # 释放相关资源
            # release stream source object before return
            streamSource.contents.release(streamSource)
            return -1

        # Sleep 1秒
        # sleep 1 second
        time.sleep(1)

        # 软触发取一张图
        # execute software trigger to grab one frame
        nRet = grabOne(camera)
        if nRet != 0:
            print("grabOne fail!")
            # 释放相关资源
            # release stream source object before return
            streamSource.contents.release(streamSource)
            return -1
        else:
            print("trigger time: " + str(datetime.datetime.now()))

        # 停止拉流
        # stop grabbing
        nRet = streamSource.contents.stopGrabbing(streamSource)
        if nRet != 0:
            print("stopGrabbing fail!")
            # 释放相关资源
            # release stream source object before return
            streamSource.contents.release(streamSource)
            return -1
        pass

    def save_bmp_clicked(self):
        # 主动取图
        # get one frame
        frame = pointer(GENICAM_Frame())
        nRet = streamSource.contents.getFrame(streamSource, byref(frame), c_uint(1000))
        if nRet != 0:
            print("SoftTrigger getFrame fail! timeOut [1000]ms")
            # 释放相关资源
            # release stream source object before return
            streamSource.contents.release(streamSource)
            return -1
        else:
            print("SoftTrigger getFrame success BlockId = " + str(frame.contents.getBlockId(frame)))
            print("get frame time: " + str(datetime.datetime.now()))

        nRet = frame.contents.valid(frame)
        if nRet != 0:
            print("frame is invalid!")
            # 释放驱动图像缓存资源
            # release frame resource before return
            frame.contents.release(frame)
            # 释放相关资源
            # release stream source object before return
            streamSource.contents.release(streamSource)
            return -1

            # 将裸数据图像拷出
        # copy image data out from frame
        imageSize = frame.contents.getImageSize(frame)
        buffAddr = frame.contents.getImage(frame)
        frameBuff = c_buffer(b'\0', imageSize)
        memmove(frameBuff, c_char_p(buffAddr), imageSize)

        # 给转码所需的参数赋值
        # fill conversion parameter
        convertParams = IMGCNV_SOpenParam()
        convertParams.dataSize = imageSize
        convertParams.height = frame.contents.getImageHeight(frame)
        convertParams.width = frame.contents.getImageWidth(frame)
        convertParams.paddingX = frame.contents.getImagePaddingX(frame)
        convertParams.paddingY = frame.contents.getImagePaddingY(frame)
        convertParams.pixelForamt = frame.contents.getImagePixelFormat(frame)

        # 释放驱动图像缓存
        # release frame resource at the end of use
        frame.contents.release(frame)

        # 保存bmp图片
        # save bmp image
        bmpInfoHeader = BITMAPINFOHEADER()
        bmpFileHeader = BITMAPFILEHEADER()

        uRgbQuadLen = 0
        rgbQuad = (RGBQUAD * 256)()  # 调色板信息 | color palette info
        rgbBuff = c_buffer(b'\0', convertParams.height * convertParams.width * 3)

        # 如果图像格式是 Mono8 不需要转码
        # no format conversion required for Mono8
        if convertParams.pixelForamt == EPixelType.gvspPixelMono8:
            # 初始化调色板rgbQuad 实际应用中 rgbQuad 只需初始化一次
            # initialize color palette
            for i in range(0, 256):
                rgbQuad[i].rgbBlue = rgbQuad[i].rgbGreen = rgbQuad[i].rgbRed = i;

            uRgbQuadLen = sizeof(RGBQUAD) * 256
            bmpFileHeader.bfSize = sizeof(bmpFileHeader) + sizeof(bmpInfoHeader) + uRgbQuadLen + convertParams.dataSize
            bmpInfoHeader.biBitCount = 8
        else:
            # 转码 => BGR24
            # convert to BGR24
            rgbSize = c_int()
            nRet = IMGCNV_ConvertToBGR24(cast(frameBuff, c_void_p), byref(convertParams), \
                                         cast(rgbBuff, c_void_p), byref(rgbSize))

            if nRet != 0:
                print("image convert fail! errorCode = " + str(nRet))
                # 释放相关资源
                # release stream source object before return
                streamSource.contents.release(streamSource)
                return -1

            bmpFileHeader.bfSize = sizeof(bmpFileHeader) + sizeof(bmpInfoHeader) + rgbSize.value
            bmpInfoHeader.biBitCount = 24

        bmpFileHeader.bfType = 0x4D42  # 文件头类型 'BM'(42 4D) | file type,  must be BM
        bmpFileHeader.bfReserved1 = 0  # 保留字 | reserved
        bmpFileHeader.bfReserved2 = 0  # 保留字 | reserved
        bmpFileHeader.bfOffBits = 54 + uRgbQuadLen  # 位图像素数据的起始位置 | offset from the beginning of the BITMAPFILEHEADER structure to the bitmap bits

        bmpInfoHeader.biSize = 40  # 信息头所占字节数 | number of bytes required by the structure
        bmpInfoHeader.biWidth = convertParams.width
        bmpInfoHeader.biHeight = -convertParams.height
        bmpInfoHeader.biPlanes = 1  # 位图平面数| number of planes

        bmpInfoHeader.biCompression = 0  # 压缩类型，0 即不压缩 | compression type
        bmpInfoHeader.biSizeImage = 0
        bmpInfoHeader.biXPelsPerMeter = 0
        bmpInfoHeader.biYPelsPerMeter = 0
        bmpInfoHeader.biClrUsed = 0
        bmpInfoHeader.biClrImportant = 0

        fileName = './image/image.bmp'
        imageFile = open(fileName, 'wb+')

        imageFile.write(struct.pack('H', bmpFileHeader.bfType))
        imageFile.write(struct.pack('I', bmpFileHeader.bfSize))
        imageFile.write(struct.pack('H', bmpFileHeader.bfReserved1))
        imageFile.write(struct.pack('H', bmpFileHeader.bfReserved2))
        imageFile.write(struct.pack('I', bmpFileHeader.bfOffBits))

        imageFile.write(struct.pack('I', bmpInfoHeader.biSize))
        imageFile.write(struct.pack('i', bmpInfoHeader.biWidth))
        imageFile.write(struct.pack('i', bmpInfoHeader.biHeight))
        imageFile.write(struct.pack('H', bmpInfoHeader.biPlanes))
        imageFile.write(struct.pack('H', bmpInfoHeader.biBitCount))
        imageFile.write(struct.pack('I', bmpInfoHeader.biCompression))
        imageFile.write(struct.pack('I', bmpInfoHeader.biSizeImage))
        imageFile.write(struct.pack('i', bmpInfoHeader.biXPelsPerMeter))
        imageFile.write(struct.pack('i', bmpInfoHeader.biYPelsPerMeter))
        imageFile.write(struct.pack('I', bmpInfoHeader.biClrUsed))
        imageFile.write(struct.pack('I', bmpInfoHeader.biClrImportant))

        if convertParams.pixelForamt == EPixelType.gvspPixelMono8:
            # 写入调色板信息
            # write out color palette info
            for i in range(0, 256):
                imageFile.write(struct.pack('B', rgbQuad[i].rgbBlue))
                imageFile.write(struct.pack('B', rgbQuad[i].rgbGreen))
                imageFile.write(struct.pack('B', rgbQuad[i].rgbRed))
                imageFile.write(struct.pack('B', rgbQuad[i].rgbReserved))

            imageFile.writelines(frameBuff)
        else:
            imageFile.writelines(rgbBuff)

        imageFile.close()
        print("save " + fileName + " success.")
        print("save bmp time: " + str(datetime.datetime.now()))
        pass

    def get_paramater_clicked(self):
        exposure_time = 0
        nRet = getExposureTime(camera, exposure_time)
        self.ui.ExposureTime.setText(exposure_time)
        if nRet != 0:
            print("set ExposureTime fail")
            # 释放相关资源
            # release stream source object before return
            streamSource.contents.release(streamSource)
            return -1
        pass

    def set_paramater_clicked(self):
        # 设置曝光
        # set ExposureTime
        nRet = setExposureTime(camera, self.ui.ExposureTime.toString())
        if nRet != 0:
            print("set ExposureTime fail")
            # 释放相关资源
            # release stream source object before return
            streamSource.contents.release(streamSource)
            return -1
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
