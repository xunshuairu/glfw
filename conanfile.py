from conans import ConanFile, CMake, tools
import os
class GlfwConan(ConanFile):
    name = "glfw"
    version = "3.2.1"
    author = "xunshuairu"
    url = "https://github.com/xunshuairu/glfw"
    license = "Zlib"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "src/*", "include/*", "deps/*"

    def package(self):
        self.copy("*.h", "include", "include", keep_path=True)
        self.copy("*.h", "include", "deps", keep_path=True)
        self.copy("*.c", "include", "deps", keep_path=True)
        self.copy("*.dll", dst="bin", src="src") # From bin to bin
        self.copy("*.dylib*", dst="bin", src="src") # From lib to bin
        self.copy("*.a", dst="lib", src="src") # From lib to bin
        self.copy("*.so", dst="lib", src="src") # From lib to bin
        self.copy("*.lib", dst="lib", src="src") # From lib to bin

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package_info(self):
        self.cpp_info.libs = ["glfw3"]