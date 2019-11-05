from conans import ConanFile, CMake, tools

import os

class QtXlsxWriterConan(ConanFile):
    name = "qtxlsxwriter"
    version="0.0.0" # master
    license = "MIT"
    url = "https://github.com/vaerizk/conan-qtxlsxwriter"
    homepage = "https://github.com/VSRonin/QtXlsxWriter"
    description = "A library that can read and write Excel files"
    topics = ("qtxlsxwriter", "excel", "xlsx", "conan-recipe")

    settings = {
        "os": ["Windows"],
        "compiler": None,
        "build_type": None,
        "arch": None
    }
    options = {"shared": [True]}
    default_options = {
        "shared": True
    }
    generators = "cmake_paths"
    no_copy_source = True

    _commit_hash = "d3bd83b064ab89215bf9a78333e5d3f89d47467b"
    _source_subdir_name = "source_subdir"

    def build_requirements(self):
        self.build_requires("cmake_installer/[>3.0.0]@conan/stable")

    def requirements(self):
        self.requires("qt/[>5.5]@bincrafters/stable", private=False)

    def source(self):
        url = "https://github.com/VSRonin/QtXlsxWriter/archive/{}.zip".format(self._commit_hash)
        tools.get(url)
        os.rename("QtXlsxWriter-{}".format(self._commit_hash), self._source_subdir_name)

    def build(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_TOOLCHAIN_FILE"] = os.path.join(self.build_folder, "conan_paths.cmake")
        cmake.configure(source_folder=self._source_subdir_name)
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self._source_subdir_name)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
