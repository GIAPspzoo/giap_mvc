# -*- coding: utf-8 -*-

import os

from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QMessageBox

from qgis.utils import iface


class GiapMVCModel(QSqlTableModel):
    def __init__(self):
        super(GiapMVCModel, self).__init__()

    @staticmethod
    def get_database(database_path, con_name):
        """
        Set connection to database file.
        :return: QSqlDatabase
        """
        dbfile = os.path.normpath(database_path)
        db = QSqlDatabase.addDatabase('QSPATIALITE', con_name)
        db.setDatabaseName(dbfile)
        db.open()
        return db

    @staticmethod
    def check_database_connection(database):
        if not database:
            QMessageBox.warning(iface,
                                "Uwaga",
                                "Nie udało się podłączyć bazy.")

    @staticmethod
    def get_sqlmodel(database, table_name):
        """
        Prepares table model for further usage.
        :param table_name: String name of sql table
        :param database: QSqlDatabase
        :return: QSqlTableModel
        """
        sqlmodel = QSqlTableModel(db=database)
        sqlmodel.setTable(table_name)
        sqlmodel.setEditStrategy(QSqlTableModel.OnManualSubmit)
        sqlmodel.select()
        while sqlmodel.canFetchMore():
            sqlmodel.fetchMore()
        return sqlmodel

    @staticmethod
    def set_headers(model, headers):
        """
        Set 'human' headers for model columns
        :param model: QAbstractItemModel
        :param headers: dict
        """
        for header, column in headers.items():
            model.setHeaderData(column, Qt.Horizontal, header)


class RoadsModel(GiapMVCModel):
    cols_headers = {
        'Odcinek drogi': 1,
        'Numer drogi': 2,
        'Nazwa drogi': 3,
        'Kategoria': 4,
        'Klasa': 5,
        'Organ zarządzający': 6,
        'Nawierzchnia': 7,
        'Stan nawierzchni': 8,
        'Liczba pasów': 9,
        'Pas awaryjny': 10,
        'Liczba pasów awaryjnych': 11,
        'Data aktualizacji': 12,
        'Status': 13,
        'Uwagi': 14,
        'Liczba jezdni': 20,
        'Numer jezdni': 21,
        'Jednokierunkowa': 22,
    }
    database_path = 'C:/Users/pajton3/Desktop/drogowiec.sqlite'
    table_name = 'drogi'

    def __init__(self):
        super(RoadsModel).__init__()
        self.db = self.get_database(self.database_path, 'drogowiec')
        self.check_database_connection(self.db)


class AddressPointsModel(GiapMVCModel):
    cols_headers = {
        'Numer GML': 1,
        'Numer lokalny': 2,
        'Przestrzeń': 3,
        'Numer wersji': 4,
        'Województwo': 7,
        'Powiat': 8,
        'Gmina': 9,
        'Numer porządkowy': 10,
        'Numer lokalu': 11,
        'Nazwa jednostki': 12,
        'Rodzaj jednostki': 13,
        'Kod pocztowy': 14,
        'Ważny od': 20,
        'Ważny do': 21,
    }
    database_path = 'C:/Users/pajton3/Desktop/pkt_adresowe.sqlite'
    table_name = 'AD_PunktAdresowy'

    def __init__(self):
        super(AddressPointsModel).__init__()
        self.db = self.get_database(self.database_path, 'adresat')
        self.check_database_connection(self.db)
