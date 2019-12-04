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
        self.mapper_dict = {
            self.lineEdit: 2,
            self.doubleSpinBox: 20,
            self.comboBox: 4,
            self.lineEdit_auto: 13,
            self.plainTextEdit: 14,
        }

    def set_mapper(self, model, headers):
        """
        Establish connection between model columns and dialog objects
        :param model: model from tableview
        :param headers: dict with column names and numbers
        """
        self.mapper.setSubmitPolicy(QtWidgets.QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(model)
        for mapped_obj, column in self.mapper_dict.items():
            self.mapper.addMapping(mapped_obj, column)

    def reset_mapper(self):
        self.doubleSpinBox.setValue(0.00)
        self.comboBox.setCurrentIndex(0)
