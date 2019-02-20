from conans import ConanFile, CMake

class GlfwConan(ConanFile):
    name = "glfw"
    version = "3.2.1"
    author = "xunshuairu"
    url = "https://github.com/xunshuairu/glfw"
    license = "Zlib"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def package(self):
        self.copy("*.dll", dst="bin", src="src") # From bin to bin
        self.copy("*.dylib*", dst="bin", src="src") # From lib to bin
        self.copy("*.a*", dst="bin", src="src") # From lib to bin
        self.copy("*.so*", dst="bin", src="src") # From lib to bin
        self.copy("*.lib*", dst="bin", src="src") # From lib to bin

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package_info(self):
        self.cpp_info.libs = self.collect_libs()