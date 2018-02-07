from conans import ConanFile, CMake, tools
import os
from glob import glob


class vtkConan(ConanFile):
    name = "vtk"
    version = "7.1.1"
    description = "The Visualization Toolkit (VTK) is an open-source, \
        freely available software system for 3D computer graphics, \
        image processing, and visualization."
    homepage = "https://www.vtk.org/"
    url = "https://gitlab.kitware.com/vtk/vtk"
    license = "BSD license"
    short_paths = True
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "Module_vtkRenderingExternal": [True, False]
    }
    default_options = "shared=True", "Module_vtkRenderingExternal=False"

    def source(self):
        tools.get("%s/repository/v%s/archive.zip" % (self.url, self.version))
        os.rename(glob("vtk-v%s-*" % self.version)[0], "sources")

    def package(self):
        self.copy("copyright*", dst="licenses",
                  src="sources", ignore_case=True)
        self.copy("*license*", dst="licenses", src="sources", ignore_case=True)
        self.copy("*.H", dst="include", src="sources")
        self.copy("*.h", dst="include", src="sources")
        self.copy("*.hh", dst="include", src="sources")
        self.copy("*.hpp", dst="include", src="sources")
        self.copy("*.hxx", dst="include", src="sources")
        self.copy("*.h++", dst="include", src="sources")
        self.copy("*.ii", dst="include", src="sources")
        self.copy("*.ixx", dst="include", src="sources")
        self.copy("*.ipp", dst="include", src="sources")
        self.copy("*.inl", dst="include", src="sources")
        self.copy("*.txx", dst="include", src="sources")
        self.copy("*.tpp", dst="include", src="sources")
        self.copy("*.tpl", dst="include", src="sources")
        self.copy("*.H", dst="include", excludes="sources")
        self.copy("*.h", dst="include", excludes="sources")
        self.copy("*.hh", dst="include", excludes="sources")
        self.copy("*.hpp", dst="include", excludes="sources")
        self.copy("*.hxx", dst="include", excludes="sources")
        self.copy("*.h++", dst="include", excludes="sources")
        self.copy("*.ii", dst="include", excludes="sources")
        self.copy("*.ixx", dst="include", excludes="sources")
        self.copy("*.ipp", dst="include", excludes="sources")
        self.copy("*.inl", dst="include", excludes="sources")
        self.copy("*.txx", dst="include", excludes="sources")
        self.copy("*.tpp", dst="include", excludes="sources")
        self.copy("*.tpl", dst="include", excludes="sources")

        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")  # From bin to bin
        self.copy("*.dylib*", dst="lib", src="lib")  # From lib to bin

    def build(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_EXAMPLES"] = "OFF"
        cmake.definitions["BUILD_TESTING"] = "OFF"
        cmake.definitions["BUILD_DOCUMENTATION"] = "OFF"
        cmake.definitions["Module_vtkRenderingExternal"] = "ON" if self.options.Module_vtkRenderingExternal else "OFF"
        cmake.configure(source_folder="sources")
        cmake.build()

        # if self.settings.os == "Linux":
        #     self.run("sudo apt-get update && sudo apt-get install -y \
        #         freeglut3-dev \
        #         mesa-common-dev \
        #         mesa-utils-extra \
        #         libgl1-mesa-dev \
        #         libglapi-mesa")

    def package_info(self):
        lib_version = ("%s.%s" % (self.version.split('.')
                                  [0], self.version.split('.')[1]))

        libs = [
            "vtkalglib",
            "vtkChartsCore",
            "vtkCommonColor",
            "vtkCommonComputationalGeometry",
            "vtkCommonCore",
            "vtkCommonDataModel",
            "vtkCommonExecutionModel",
            "vtkCommonMath",
            "vtkCommonMisc",
            "vtkCommonSystem",
            "vtkCommonTransforms",
            "vtkDICOMParser",
            "vtkDomainsChemistry",
            "vtkDomainsChemistryOpenGL2",
            "vtkexoIIc",
            "vtkexpat",
            "vtkFiltersAMR",
            "vtkFiltersCore",
            "vtkFiltersExtraction",
            "vtkFiltersFlowPaths",
            "vtkFiltersGeneral",
            "vtkFiltersGeneric",
            "vtkFiltersGeometry",
            "vtkFiltersHybrid",
            "vtkFiltersHyperTree",
            "vtkFiltersImaging",
            "vtkFiltersModeling",
            "vtkFiltersParallel",
            "vtkFiltersParallelImaging",
            "vtkFiltersPoints",
            "vtkFiltersProgrammable",
            "vtkFiltersSelection",
            "vtkFiltersSMP",
            "vtkFiltersSources",
            "vtkFiltersStatistics",
            "vtkFiltersTexture",
            "vtkFiltersVerdict",
            "vtkfreetype",
            "vtkGeovisCore",
            "vtkgl2ps",
            "vtkglew",
            "vtkhdf5_hl",
            "vtkhdf5",
            "vtkImagingColor",
            "vtkImagingCore",
            "vtkImagingFourier",
            "vtkImagingGeneral",
            "vtkImagingHybrid",
            "vtkImagingMath",
            "vtkImagingMorphological",
            "vtkImagingSources",
            "vtkImagingStatistics",
            "vtkImagingStencil",
            "vtkInfovisCore",
            "vtkInfovisLayout",
            "vtkInteractionImage",
            "vtkInteractionStyle",
            "vtkInteractionWidgets",
            "vtkIOAMR",
            "vtkIOCore",
            "vtkIOEnSight",
            "vtkIOExodus",
            "vtkIOExport",
            "vtkIOGeometry",
            "vtkIOImage",
            "vtkIOImport",
            "vtkIOInfovis",
            "vtkIOLegacy",
            "vtkIOLSDyna",
            "vtkIOMINC",
            "vtkIOMovie",
            "vtkIONetCDF",
            "vtkIOParallel",
            "vtkIOParallelXML",
            "vtkIOPLY",
            "vtkIOSQL",
            "vtkIOTecplotTable",
            "vtkIOVideo",
            "vtkIOXML",
            "vtkIOXMLParser",
            "vtkjpeg",
            "vtkjsoncpp",
            "vtklibxml2",
            "vtkmetaio",
            "vtkNetCDF_cxx",
            "vtkNetCDF",
            "vtkoggtheora",
            "vtkParallelCore",
            "vtkpng",
            "vtkproj4",
            "vtkRenderingAnnotation",
            "vtkRenderingContext2D",
            "vtkRenderingContextOpenGL2",
            "vtkRenderingCore",
            "vtkRenderingFreeType",
            "vtkRenderingImage",
            "vtkRenderingLabel",
            "vtkRenderingLOD",
            "vtkRenderingOpenGL2",
            "vtkRenderingVolume",
            "vtkRenderingVolumeOpenGL2",
            "vtksqlite",
            "vtksys",
            "vtktiff",
            "vtkverdict",
            "vtkViewsContext2D",
            "vtkViewsCore",
            "vtkViewsInfovis",
            "vtkzlib"
        ]

        if self.options.Module_vtkRenderingExternal:
            libs.append("vtkRenderingExternal")

        for i, lib in enumerate(libs):
            libs[i] = ("%s-%s" % (lib, lib_version))

        self.cpp_info.libs = libs

        self.cpp_info.includedirs = list()

        for dirpath, dirs, files in os.walk("include"):
            self.cpp_info.includedirs.append(dirpath)
