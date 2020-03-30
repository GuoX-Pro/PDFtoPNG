# PDF&WORD转PNG执行程序
# -*- coding: utf-8 -*-
import os , fitz # PyMuPDF
class conver:
#建立转换类
   def __init__(self,sname,pngpath,mark):
       #初始化
       self.pngpath = pngpath
       self.sname = sname
       self.tname = sname
       self.mark = mark
       self.count = 1
   def conver(self):
       if self.mark == 1:
          #WORD转PDF
          self.tname = self.pngpath + "\\temp.pdf"
          from win32com.client import Dispatch
          word = Dispatch('Word.Application')
          doc = word.Documents.Open(self.sname)
          doc.SaveAs(self.tname, FileFormat=17)
          doc.Close()
          word.Quit()
       #PDF转PNG
       PDFDoc = fitz.open(self.tname)
       self.count = PDFDoc.pageCount
       for pg in range(PDFDoc.pageCount):
           page = PDFDoc[pg]
           rotate = int(0)
           # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
           # 此处若是不做设置，默认图片大小为：792X612, dpi=96
           zoom_x = 4  # (1.33333333-->1056x816)   (2-->1584x1224)
           zoom_y = 4
           mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
           pix = page.getPixmap(matrix=mat, alpha=False)
           temppath, tempfilename = os.path.split(self.sname)
           tempfilename, temppath = os.path.splitext(tempfilename)

           if PDFDoc.pageCount == 1:  # 判断页数
               pix.writePNG(self.pngpath + '\\' + '%s.png' % tempfilename)  # 将图片写入指定的文件夹内
           else:
               if not os.path.exists(self.pngpath + '\\%s' % tempfilename):
                   os.makedirs(self.pngpath + '\\%s' % tempfilename)
               pix.writePNG(self.pngpath + '\\%s\\%s.png' % (tempfilename, pg + 1))
       del(PDFDoc)
       if self.mark == 1:
          os.remove(self.tname)