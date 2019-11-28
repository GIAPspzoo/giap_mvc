# -*- coding: utf-8 -*-

import os

from PyQt5 import QtWidgets, uic

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'road_view_base.ui'))


class RoadView(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        super(RoadView, self).__init__(parent)
        self.setupUi(self)
        self.mapper = QtWidgets.QDataWidgetMapper(self)

    def set_mapper(self, model, headers):
        """

        :param model:
        :param headers:
        """
        self.mapper.setSubmitPolicy(QtWidgets.QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(model)
        self.mapper.addMapping(self.lineEdit, headers['Numer drogi'])
        self.mapper.addMapping(self.doubleSpinBox, headers['Liczba jezdni'])
        self.mapper.addMapping(self.comboBox, headers['Kategoria'])
        self.mapper.addMapping(self.lineEdit_auto, headers['Status'])
        self.mapper.addMapping(self.plainTextEdit, headers['Uwagi'])

    def reset_mapper(self):
        self.doubleSpinBox.setValue(0.00)
        self.comboBox.setCurrentIndex(0)
