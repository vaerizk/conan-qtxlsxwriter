cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

find_package(QtXlsxWriter REQUIRED)
find_package(Qt5 5.5 REQUIRED Core Gui)

add_executable(example example.cpp)

include_directories(
	${QtXlsxWriter_INCLUDE_DIRS}
	${Qt5Core_INCLUDE_DIRS}
	${Qt5Gui_INCLUDE_DIRS}
	${Qt5Gui_PRIVATE_INCLUDE_DIRS}
)

target_link_libraries(example
	${QtXlsxWriter_LIBS}
	${Qt5Core_LIBRARIES}
	${Qt5Gui_LIBRARIES}
)
