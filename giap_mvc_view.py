# -*- coding: utf-8 -*-

import os

from PyQt5 import QtCore, QtWidgets, uic

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'giap_mvc_view_base.ui'))


class GiapMVCView(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        super(GiapMVCView, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window)

    def hide_columns(self, columns_count, shown_columns):
        """
        Hide model columns from tableview
        :param columns_count: column count
        :param shown_columns: list of visible columns
        """
        for column in range(columns_count):
            if column not in shown_columns:
                self.tableView.hideColumn(column)

    def reset_view(self, model):
        self.tableView.setModel(model)
