import sys
from PyQt4 import QtCore, QtGui

class ExclusiveModel(QtGui.QStandardItemModel):
    def __init__(self, parent=None):
        QtGui.QStandardItemModel.__init__(self, parent)

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        # Call base class method
        print index, value
        return_value = QtGui.QStandardItemModel.setData(self, index, 
value, role)

        # Check if all other items must be unchecked
#         if role == QtCore.Qt.CheckStateRole:
#             changed_item = self.itemFromIndex(index)

#             if changed_item.checkState() == QtCore.Qt.Checked:
#                 for row in range(self.rowCount()):
#                     item = self.item(row, 0)
#                     if item.text() != changed_item.text():
#                         new_value = QtCore.QVariant(QtCore.Qt.Unchecked)
#                         new_index = self.indexFromItem(item)
#                         QtGui.QStandardItemModel.setData(self, 
# new_index, new_value, role)

        return return_value
               
class View(QtGui.QTreeView):
    """
       Class for defining a widget for holding the analysis and 
calculator views.
    """
    def __init__(self, parent=None):
        """
           Constructor.
        """
        # Call base class constructor
        QtGui.QTreeView.__init__(self, parent)

        # model
        self._model = ExclusiveModel()
        for value in ['Why', 'does', 'this', 'not', 'work', 'does', 'this', 'not', 'work', 'does', 'this', 'not', 'work', 'does', 'this', 'not', 'work']:
            item = QtGui.QStandardItem(value)
            item.setCheckable(True)
            self._model.appendRow([item])

        # Add the elements
        self.setModel(self._model)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    widget = View()
    widget.show()

    sys.exit(app.exec_())