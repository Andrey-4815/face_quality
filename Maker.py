
import datetime, os, threading, time, traceback, openpyxl, requests, sys, chime, shutil
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image, ImageDraw
from datetime import timedelta

from Reqests import Reqests


class Maker(Reqests):

    def save_chart(self):
        self.label_15.setText(f"Готово 0/{len(self.cameras)}")
        self.dir = f"{self.dir}\\report_{datetime.datetime.now().strftime('%d.%m.%Y %H.%M.%S')}"
        os.makedirs(f"{self.dir}\\heat_map")
        os.mkdir(f"{self.dir}\\orig_photo")
        os.mkdir(f"{self.dir}\\map_with_backing")
        os.mkdir(f"{self.dir}\\face_in_photo")
        Wordbook = openpyxl.Workbook()
        sheet = Wordbook['Sheet']
        sheet.title = "Отчет"
        sheet.cell(1, 1).value = "id камеры"
        sheet.cell(1, 2).value = "Имя камеры"
        sheet.cell(1, 3).value = "Количество детектов"
        sheet.cell(1, 4).value = "Средний размер лица"
        sheet.cell(1, 5).value = "Среднее качество"
        time_start = (datetime.datetime.now() - timedelta(self.days, hours=3)).strftime("%Y-%m-%dT%H:%M:%SZ")

        for index, cam_id in enumerate(self.cameras):
            if not self.Flag:
                return
            try:
                sheet.cell(sheet.max_row + 1, 1).value = cam_id
                self.camera_name = self.get_cam_name(cam_id)
                if not self.camera_name:
                    sheet.cell(sheet.max_row, 2).value = "Не нашел такую камеру"
                    continue

                self.res = self.get_quality_detects(cam_id, 10000, time_start)
                if self.res.get("faces") == []:
                    sheet.cell(sheet.max_row, 2).value = self.camera_name
                    sheet.cell(sheet.max_row, 3).value = "Нет детектов"
                    continue
                response = requests.get(f'{self.res.get("faces")[0].get("photo")}')
                self.datafile = Image.open(BytesIO(response.content))
                self.datafile.save(f'{self.dir}\\orig_photo\\{self.camera_name}.png')

                if self.flag_heat_map == 2 or self.flag_map_with_backing == 2:
                    self.label.setText("Подготовка тепловой карты...")
                    time.sleep(0.1)
                    self.make_heat_map()
                if self.flag_face_in_photo == 2:
                    self.label.setText("Подготовка визуализации лиц на камере...")
                    time.sleep(0.1)
                    self.make_face_in_photo()

                self.make_report()

                sheet.cell(sheet.max_row, 2).value = self.camera_name
                sheet.cell(sheet.max_row, 3).value = len(self.res.get("faces"))
                sheet.cell(sheet.max_row, 4).value = int(self.bbox / (self.count + 1))
                sheet.cell(sheet.max_row, 5).value = self.quality / self.count_faces
                if self.flag_orig == 2:
                    sheet.cell(sheet.max_row, self.get_filled_cols(sheet, sheet.max_row)).value = '=HYPERLINK("{0}", "{1}")'.format(
                        f"orig_photo/{self.camera_name}.png", "фото с камеры")
                if self.flag_heat_map == 2:
                    sheet.cell(sheet.max_row, self.get_filled_cols(sheet, sheet.max_row)).value = '=HYPERLINK("{0}", "{1}")'.format(
                        f"heat_map/{self.camera_name}.png", "тепловая карта")
                if self.flag_map_with_backing == 2:
                    sheet.cell(sheet.max_row, self.get_filled_cols(sheet, sheet.max_row)).value = '=HYPERLINK("{0}", "{1}")'.format(
                        f"map_with_backing/{self.camera_name}.png", "карта с подложкой")
                if self.flag_face_in_photo == 2:
                    sheet.cell(sheet.max_row, self.get_filled_cols(sheet, sheet.max_row)).value = '=HYPERLINK("{0}", "{1}")'.format(
                        f"face_in_photo/{self.camera_name}.png", "лица на камере")

            except Exception as ex:
                traceback.print_exc()
                sheet.cell(sheet.max_row, 2).value = "Ошибка обработки"
            finally:
                self.label_15.setText(f"Готово {index + 1} / {len(self.cameras)}")

        if self.flag_heat_map == 0:
            shutil.rmtree(f"{self.dir}\\heat_map")
        if self.flag_orig == 0:
            shutil.rmtree(f"{self.dir}\\orig_photo")
        if self.flag_map_with_backing == 0:
            shutil.rmtree(f"{self.dir}\\map_with_backing")
        if self.flag_face_in_photo == 0:
            shutil.rmtree(f"{self.dir}\\face_in_photo")

        Wordbook.save(f'{self.dir}/Качество лиц.xlsx')
        self.label.setText("")
        self.progressBar_2.setValue(0)
        self.label_15.setText(f"Готово 0/0")
        self.textBrowser_2.append("Готово!")
        chime.success()


    def make_heat_map(self):
        mas = np.array([[0] * 1320] * 760)
        if len(self.res.get("faces")) > self.count_results:
            self.progressBar_2.setMaximum(self.count_results)
        else:
            self.progressBar_2.setMaximum(len(self.res.get("faces")))

        for count, face in enumerate(self.res.get("faces")):
            if not self.Flag:
                return
            self.progressBar_2.setValue(count)
            zone = [face.get("bbox").get("left"), face.get("bbox").get("top"),
                    face.get("bbox").get("right"), face.get("bbox").get("bottom")]
            zone = [(int(zone[0]) + 20), (int(zone[1]) + 20), (int(zone[2]) + 20), (int(zone[3]) + 20)]
            centr = int((zone[2] - zone[0]) / 2)
            a = 10.0
            for j in range(zone[0] + centr, zone[0], -1):
                b = a
                for i in range(zone[1] + centr, zone[1], -1):
                    mas[i, j] += a
                    a = a / 1.01
                a = b / 1.01

            a = 10.0 / 1.01
            for j in range(zone[0] + centr + 1, zone[2]):
                b = a
                for i in range(zone[1] + centr - 1, zone[1], -1):
                    mas[i, j] += a
                    a = a / 1.01
                a = b / 1.01

            a = 10.0 / 1.01
            for j in range(zone[0] + centr - 1, zone[0], -1):
                b = a
                for i in range(zone[1] + centr + 1, zone[3]):
                    mas[i, j] += a
                    a = a / 1.01
                a = b / 1.01

            a = 10.0
            for j in range(zone[0] + centr, zone[2]):
                b = a
                for i in range(zone[1] + centr, zone[3]):
                    mas[i, j] += a
                    a = a / 1.01
                a = b / 1.01
            mas[zone[1] + centr, zone[0] + centr] -= 1
            if count == self.count_results:
                break

        plt.imshow(mas, cmap='inferno', interpolation='nearest')
        plt.axis('off')
        plt.savefig(f'{self.dir}/heat_map/{self.camera_name}.png', dpi=300, transparent=True)
        if self.flag_map_with_backing == 2:
            self.make_map_with_backing()


    def make_face_in_photo(self):
        self.progressBar_2.setValue(0)

        img =  self.datafile.load()
        draw = ImageDraw.Draw(self.datafile)
        if len(self.res.get("faces")) > self.count_results:
            self.progressBar_2.setMaximum(self.count_results)
        else:
            self.progressBar_2.setMaximum(len(self.res.get("faces")))

        for count, face in enumerate(self.res.get("faces")):
            self.progressBar_2.setValue(count)
            response = requests.get(f'{face.get("photo")}')
            datafile1 = Image.open(BytesIO(response.content))
            pix = datafile1.load()
            zone = [face.get("bbox").get("left"), face.get("bbox").get("top"),
                    face.get("bbox").get("right"), face.get("bbox").get("bottom")]
            zone = [(int(zone[0])), (int(zone[1])), (int(zone[2])), (int(zone[3]))]
            for j in range(zone[0], zone[2]):
                for i in range(zone[1], zone[3]):
                    img[j, i] = pix[j, i]
            if count == self.count_results:
                break
            draw.rectangle((zone[0], zone[1], zone[2], zone[3]), outline=(0, 128, 0))
        self.datafile.save(f'{self.dir}/face_in_photo/{self.camera_name}.png')


    def make_report(self):
        self.quality = 0
        self.count_faces = 0
        self.bbox = 0
        for self.count, face in enumerate(self.res.get("faces")):
            try:
                self.bbox += (face.get("bbox").get("right") - face.get("bbox").get("left")) * (
                        face.get("bbox").get("bottom") - face.get("bbox").get("top"))
                if face.get("features").get("quality").get("synesis", 0) > 0:
                    self.quality += face.get("features").get("quality").get("synesis")
                    self.count_faces += 1
                if face.get("features").get("quality").get("visionlabs", 0) > 0:
                    self.quality += face.get("features").get("quality").get("visionlabs")
                    self.count_faces += 1
                if face.get("features").get("quality").get("tevian", 0) > 0:
                    self.quality += face.get("features").get("quality").get("tevian")
                    self.count_faces += 1
                if face.get("features").get("quality").get("ntechlab", 0) > 0:
                    self.quality += face.get("features").get("quality").get("ntechlab")
                    self.count_faces += 1
            except:
                pass


    def make_map_with_backing(self):
        heat = Image.open(f'{self.dir}\\heat_map\\{self.camera_name}.png')
        heat_crop = heat.crop((260, 319, 1707, 1135))
        width = 1280
        height = 720
        resized_heat = heat_crop.resize((width, height), Image.LANCZOS)
        orig = Image.open(f'{self.dir}\\orig_photo\\{self.camera_name}.png')
        heat_load = resized_heat.load()
        orig_load = orig.load()
        for j in range(1280):
            for k in range(720):
                orig_load[j, k] = heat_load[j, k]
        orig.save(f'{self.dir}\\heat_map\\{self.camera_name}.png')
        heat = Image.open(f'{self.dir}\\heat_map\\{self.camera_name}.png')
        orig = Image.open(f'{self.dir}\\orig_photo\\{self.camera_name}.png')
        new_img = Image.blend(heat, orig, 0.5)
        new_img.save(f'{self.dir}\\map_with_backing\\{self.camera_name}.png')


    def creating_imeges(self):
        heat = Image.open(f'{self.dir}\\heat_map\\{self.camera_name}.png')
        heat_crop = heat.crop((260, 319, 1707, 1135))
        width = 1280
        height = 720
        resized_heat = heat_crop.resize((width, height), Image.LANCZOS)

        heat_load = resized_heat.load()
        orig_load =  self.datafile.load()
        for j in range(1280):
            for k in range(720):
                orig_load[j, k] = heat_load[j, k]
        self.datafile.save(f'{self.dir}\\heat_map\\{self.camera_name}.png')
        heat = Image.open(f'{self.dir}\\heat_map\\{self.camera_name}.png')
        orig = Image.open(f'{self.dir}\\orig_photo\\{self.camera_name}.png')
        new_img = Image.blend(heat, orig, 0.5)
        new_img.save(f'{self.dir}\\map_with_backing\\{self.camera_name}.png')


    def get_filled_cols(self, sheet, row):
        counter = 1
        while True:
            if sheet.cell(row, counter).value != None:
                counter+=1
            else:
                break
        return counter