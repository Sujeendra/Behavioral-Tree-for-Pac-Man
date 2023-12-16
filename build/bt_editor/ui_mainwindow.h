/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.12.8
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtGui/QIcon>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QFrame>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionLoad;
    QAction *actionSave;
    QAction *actionQuit;
    QAction *actionZoom_In;
    QAction *actionZoom_ut;
    QAction *actionAuto_arrange;
    QAction *actionLoadRosparam;
    QAction *actionAdd_Action;
    QAction *actionAdd_Condition;
    QWidget *centralwidget;
    QVBoxLayout *verticalLayout_2;
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout;
    QFrame *line;
    QPushButton *playButton;
    QSpacerItem *horizontalSpacer;
    QTabWidget *tabWidget;
    QMenuBar *menubar;
    QMenu *menuLoad;
    QMenu *menuZoom;
    QMenu *menuReorder;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(1117, 726);
        MainWindow->setMinimumSize(QSize(800, 600));
        actionLoad = new QAction(MainWindow);
        actionLoad->setObjectName(QString::fromUtf8("actionLoad"));
        actionSave = new QAction(MainWindow);
        actionSave->setObjectName(QString::fromUtf8("actionSave"));
        actionQuit = new QAction(MainWindow);
        actionQuit->setObjectName(QString::fromUtf8("actionQuit"));
        actionZoom_In = new QAction(MainWindow);
        actionZoom_In->setObjectName(QString::fromUtf8("actionZoom_In"));
        actionZoom_ut = new QAction(MainWindow);
        actionZoom_ut->setObjectName(QString::fromUtf8("actionZoom_ut"));
        actionAuto_arrange = new QAction(MainWindow);
        actionAuto_arrange->setObjectName(QString::fromUtf8("actionAuto_arrange"));
        actionLoadRosparam = new QAction(MainWindow);
        actionLoadRosparam->setObjectName(QString::fromUtf8("actionLoadRosparam"));
        actionAdd_Action = new QAction(MainWindow);
        actionAdd_Action->setObjectName(QString::fromUtf8("actionAdd_Action"));
        actionAdd_Condition = new QAction(MainWindow);
        actionAdd_Condition->setObjectName(QString::fromUtf8("actionAdd_Condition"));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        verticalLayout_2 = new QVBoxLayout(centralwidget);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        verticalLayout = new QVBoxLayout();
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        horizontalLayout->setContentsMargins(-1, 0, -1, 0);
        line = new QFrame(centralwidget);
        line->setObjectName(QString::fromUtf8("line"));
        line->setFrameShape(QFrame::VLine);
        line->setFrameShadow(QFrame::Sunken);

        horizontalLayout->addWidget(line);

        playButton = new QPushButton(centralwidget);
        playButton->setObjectName(QString::fromUtf8("playButton"));
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/play.png"), QSize(), QIcon::Normal, QIcon::Off);
        icon.addFile(QString::fromUtf8(":/stop.png"), QSize(), QIcon::Normal, QIcon::On);
        playButton->setIcon(icon);
        playButton->setCheckable(true);

        horizontalLayout->addWidget(playButton);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer);


        verticalLayout->addLayout(horizontalLayout);


        verticalLayout_2->addLayout(verticalLayout);

        tabWidget = new QTabWidget(centralwidget);
        tabWidget->setObjectName(QString::fromUtf8("tabWidget"));

        verticalLayout_2->addWidget(tabWidget);

        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 1117, 21));
        menuLoad = new QMenu(menubar);
        menuLoad->setObjectName(QString::fromUtf8("menuLoad"));
        menuZoom = new QMenu(menubar);
        menuZoom->setObjectName(QString::fromUtf8("menuZoom"));
        menuReorder = new QMenu(menubar);
        menuReorder->setObjectName(QString::fromUtf8("menuReorder"));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MainWindow->setStatusBar(statusbar);

        menubar->addAction(menuLoad->menuAction());
        menubar->addAction(menuZoom->menuAction());
        menubar->addAction(menuReorder->menuAction());
        menuLoad->addAction(actionLoad);
        menuLoad->addAction(actionSave);
        menuLoad->addAction(actionQuit);
        menuZoom->addAction(actionZoom_ut);
        menuZoom->addAction(actionZoom_In);
        menuReorder->addAction(actionAuto_arrange);

        retranslateUi(MainWindow);
        QObject::connect(actionQuit, SIGNAL(triggered()), MainWindow, SLOT(close()));

        tabWidget->setCurrentIndex(-1);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "Behavior Tree", nullptr));
        actionLoad->setText(QApplication::translate("MainWindow", "Load", nullptr));
#ifndef QT_NO_SHORTCUT
        actionLoad->setShortcut(QApplication::translate("MainWindow", "Ctrl+L", nullptr));
#endif // QT_NO_SHORTCUT
        actionSave->setText(QApplication::translate("MainWindow", "Save", nullptr));
#ifndef QT_NO_SHORTCUT
        actionSave->setShortcut(QApplication::translate("MainWindow", "Ctrl+S", nullptr));
#endif // QT_NO_SHORTCUT
        actionQuit->setText(QApplication::translate("MainWindow", "Quit", nullptr));
#ifndef QT_NO_SHORTCUT
        actionQuit->setShortcut(QApplication::translate("MainWindow", "Ctrl+Q", nullptr));
#endif // QT_NO_SHORTCUT
        actionZoom_In->setText(QApplication::translate("MainWindow", "Zoom Out", nullptr));
        actionZoom_ut->setText(QApplication::translate("MainWindow", "Zoom In", nullptr));
        actionAuto_arrange->setText(QApplication::translate("MainWindow", "auto-arrange", nullptr));
#ifndef QT_NO_SHORTCUT
        actionAuto_arrange->setShortcut(QApplication::translate("MainWindow", "Ctrl+O", nullptr));
#endif // QT_NO_SHORTCUT
        actionLoadRosparam->setText(QApplication::translate("MainWindow", "Load from rosparam", nullptr));
        actionAdd_Action->setText(QApplication::translate("MainWindow", "Add Action", nullptr));
        actionAdd_Condition->setText(QApplication::translate("MainWindow", "Add Condition", nullptr));
        playButton->setText(QString());
        menuLoad->setTitle(QApplication::translate("MainWindow", "File", nullptr));
        menuZoom->setTitle(QApplication::translate("MainWindow", "Zoom", nullptr));
        menuReorder->setTitle(QApplication::translate("MainWindow", "Reorder", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
