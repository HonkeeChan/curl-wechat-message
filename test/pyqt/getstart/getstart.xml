import QtQuick 2.4
import QtQuick.Window 2.2
import Qt.labs.controls 1.0
import QtQuick.Controls 1.5

Window {
    visible: true
    width: 640
    height: 480
    title: qsTr("Hello World")

    TextEdit {
        id: price_box
        x: 242
        y: 78
        width: 101
        height: 50
        text: qsTr("Text Edit")
        font.pixelSize: 12
    }

    Text {
        id: text1
        x: 165
        y: 90
        text: qsTr("Price")
        font.pixelSize: 12
    }

    SpinBox {
        id: tax_rate
        x: 242
        y: 177
        value: 20
    }

    Label {
        id: label1
        x: 165
        y: 181
        text: qsTr("Tex Rate")
    }

    Button {
        id: calc_tax_btn
        x: 255
        y: 236
        text: qsTr("Button")
    }

    TextField {
        id: results_window
        x: 222
        y: 310
        placeholderText: qsTr("Text Field")
    }

    Label {
        id: label2
        x: 253
        y: 30
        width: 134
        text: "Sales Tax Calculator"
        scale: 2.3
    }
}
