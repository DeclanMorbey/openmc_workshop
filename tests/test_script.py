
""" test_script.py: run all the examples in the openmc workshop and check each example produces the expected results.
    The example scripts open up various plots, some of which pause / block the running of this test suite.
    The running of the tests can be manually resumed by closing matplotlib and eog windows when they pop up
    run with
    pytest test_scripts.py
"""

# at the moment, we are only testing to see whether the outputs are created
# we are NOT testing to see whether the outputs are also saved locally
# this will have to be implemented

from pathlib import Path 
import os
import pytest
import unittest

cwd = os.getcwd()

class test_task_1(unittest.TestCase):
    def test_task_1_part_1(self):

        os.chdir(Path(cwd))
        os.chdir(Path('tasks/task_1'))
        output_filename = '1_example_isotope_plot.html'
        os.system('rm '+output_filename)
        os.system('python 1_example_isotope_plot.py')
        assert Path(output_filename).exists() == True
        os.system('rm '+output_filename)


    def test_task_1_part_2(self): #  this test is slow so it has been commented out for the time being

        os.chdir(Path(cwd))
        os.chdir(Path('tasks/task_1'))
        output_filename = '2_example_element_plot_16.html'
        os.system('rm '+output_filename)
        os.system('python 2_example_element_plot.py')
        assert Path(output_filename).exists() == True
        os.system('rm '+output_filename)


    def test_task_1_part_3(self):
        
        os.chdir(Path(cwd))
        os.chdir(Path('tasks/task_1'))
        output_filename = '3_example_material_plot.html'
        os.system('rm '+output_filename)
        os.system('python 3_example_material_plot.py')
        assert Path(output_filename).exists() == True
        os.system('rm '+output_filename)


class test_task_2(unittest.TestCase):
    
    def test_task_2_part_1(self): #  This test launches matplotlib that pauses the running of the script
    
        os.chdir(Path(cwd))
        os.chdir(Path('tasks/task_2'))
        output_filenames = ['xz_sphere.png', 'xy_sphere.png', 'yz_sphere.png']
        for output_filename in output_filenames:
            os.system('rm '+output_filename)
        os.system('python 1_example_geometry_viewer_2d.py')
        for output_filename in output_filenames:
            assert Path(output_filename).exists() == True
            os.system('rm '+output_filename)


    def test_task_2_part_1_optional(self): #  This test launches eog that pauses the running of the script

        os.chdir(Path(cwd))
        os.chdir(Path('tasks/task_2'))
        output_filename = 'plot.png'
        os.system('rm '+output_filename)
        os.system('python 2_example_geometry_viewer_2d_xml_version.py')
        assert Path(output_filename).exists() == True
        os.system('rm '+output_filename)


    def test_task_2_part_3(self): #  This test launches matplotlib that pauses the running of the script

        os.chdir(Path(cwd))
        os.chdir(Path('tasks/task_2'))
        output_filenames = ['xz_tokamak.png', 'xy_tokamak.png', 'yz_tokamak.png']
        for output_filename in output_filenames:
            os.system('rm '+output_filename)
        os.system('python 3_example_geometry_viewer_2d_tokamak.py')
        for output_filename in output_filenames:
            assert Path(output_filename).exists() == True
            os.system('rm '+output_filename)


    def test_task_2_part_4(self):

        os.chdir(Path(cwd))
        os.chdir(Path('tasks/task_2'))
        output_filename = 'plot_3d_tokamak.vti'
        os.system('rm '+output_filename)
        os.system('python 4_example_geometry_viewer_3d_tokamak.py')
        assert Path(output_filename).exists() == True
        os.system('rm '+output_filename)



class test_task_3(unittest.TestCase):
    def test_task_3_part_1(self):

        os.chdir(Path(cwd))
        os.chdir(Path('tasks/task_3'))
        output_filename = 'particle_energy_histogram.html'
        os.system('rm '+output_filename)
        os.system('python 1_plot_neutron_birth_energy.py')
        assert Path(output_filename).exists() == True
        os.system('rm '+output_filename)
    
    
    def test_task_3_part_2(self):

        os.chdir(Path(cwd))
        os.chdir(Path('tasks/task_3'))
        output_filename = 'particle_location.html'
        os.system('rm '+output_filename)
        os.system('python 2_plot_neutron_birth_location.py')
        assert Path(output_filename).exists() == True
        os.system('rm '+output_filename)
    

    def test_task_3_part_3(self):

        os.chdir(Path(cwd))
        os.chdir(Path('tasks/task_3'))
        output_filename = 'particle_direction.html'
        os.system('rm '+output_filename)
        os.system('python 3_plot_neutron_birth_direction.py')
        assert Path(output_filename).exists() == True
        os.system('rm '+output_filename)
    

    def test_task_3_part_4(self):

        os.chdir(Path(cwd))
        os.chdir(Path('tasks/task_3'))
        output_filename = 'plasma_particle_location.html'
        os.system('rm '+output_filename)
        os.system('python 4_plot_neutron_birth_location_plasma.py')
        assert Path(output_filename).exists() == True
        os.system('rm '+output_filename)
 

    def test_task_3_part_5(self):

        os.chdir(Path(cwd))
        os.chdir(Path('tasks/task_3'))
        output_filename = 'plasma_particle_direction.html'
        os.system('rm '+output_filename)
        os.system('python 5_plot_neutron_birth_direction_plasma.py')
        assert Path(output_filename).exists() == True
        os.system('rm '+output_filename)
        

    def test_task_3_part_6(self):

        os.chdir(Path(cwd))
        os.chdir(Path('tasks/task_3'))
        output_filenames = ['plot_3d.h5', 'plot_3d.vti', 'track_1_1_4.h5', 'track_1_1_4.pvtp', 'track_1_1_4_0.vtp']
        for output_filename in output_filenames:
            os.system('rm '+output_filename)
        os.system('python 6_example_neutron_tracks.py')
        for output_filename in output_filenames:
            assert Path(output_filename).exists() == True
            os.system('rm '+output_filename)
        


class test_task_4(unittest.TestCase):
    def test_task_4_part_1(self):

        os.chdir(Path(cwd))
        os.chdir(Path('tasks/task_4'))
        output_filenames = ['universe_plot.png', 'flux_plot.png']
        for output_filename in output_filenames:
            os.system('rm '+output_filename)
        os.system('python 1_example_neutron_flux.py')
        for output_filename in output_filenames:
            assert Path(output_filename).exists() == True
            os.system('rm '+output_filename)

    def test_task_4_part_2(self):

        os.chdir(Path(cwd))
        os.chdir(Path('tasks/task_4'))
        output_filename = 'tally_on_mesh.vtk'
        os.system('rm '+output_filename)
        os.system('python 2_example_neutron_flux_tokamak.py')
        assert Path(output_filename).exists() == True
        os.system('rm '+output_filename)
        


class test_task_5(unittest.TestCase):
    def test_task_5_part_1(self):
 
        os.chdir(Path(cwd))
        os.chdir(Path('tasks/task_5'))
        output_filename = 'tokamak_spectra.html'
        os.system('rm '+output_filename)
        os.system('python 1_example_neutron_spectra_tokamak.py')
        assert Path(output_filename).exists() == True
        os.system('rm '+output_filename)
      

    def test_task_5_part_2(self):

        os.chdir(Path(cwd))
        os.chdir(Path('tasks/task_5'))
        output_filename = 'tokamak_photon_spectra.html'
        os.system('rm '+output_filename)
        os.system('python 2_example_photon_spectra_tokamak.py')
        assert Path(output_filename).exists() == True
        os.system('rm '+output_filename)
   


class test_task_6(unittest.TestCase):
    def test_task_6_part_1(self):

        os.chdir(Path(cwd))
        os.chdir(Path('tasks/task_6'))
        output_filename = 'simulation_results.json'
        os.system('rm '+output_filename)
        os.system('python 1_example_tritium_production.py')
        assert Path(output_filename).exists() == True
        os.system('rm '+output_filename)

    def test_task_6_part_2(self):

        os.chdir(Path(cwd))
        os.chdir(Path('tasks/task_6'))
        output_filename = 'tbr_study.html'
        os.system('rm '+output_filename)
        os.system('python 2_example_tritium_production_study.py')
        assert Path(output_filename).exists() == True
        os.system('rm '+output_filename)



class test_task_7(unittest.TestCase):
    def test_task_7_part_1(self):

        os.chdir(Path(cwd))
        os.chdir(Path('tasks/task_7'))
        output_filename = '1_find_dpa_results.json'
        os.system('rm '+output_filename)
        os.system('python 1_find_dpa.py')
        assert Path(output_filename).exists() == True
        os.system('rm '+output_filename)

    def test_task_7_part_2(self):

        os.chdir(Path(cwd))
        os.chdir(Path('tasks/task_7'))
        output_filename = '2_find_cell_volume_results.json'
        os.system('rm '+output_filename)
        os.system('python 2_find_cell_volume.py')
        assert Path(output_filename).exists() == True
        os.system('rm '+output_filename)



class test_task_8(unittest.TestCase):

    def test_task_8_part_1(self):

        os.chdir(Path(cwd))
        os.chdir(Path('tasks/task_8'))
        os.system('rm outputs/*.json')
        os.system('rmdir outputs')
        os.system('python 1_simulate_with_random_sample.py')
        assert Path('outputs').exists() == True
        assert len(os.listdir('outputs')) != 0

    def test_task_8_part_2(self):

        os.chdir(Path(cwd))
        os.chdir(Path('tasks/task_8'))
        output_filenames = ['TBR_vs_enrichment_fraction.html', 'TBR_vs_thickness.html']
        for output_filename in output_filenames:
            os.system('rm '+output_filename)
        os.system('python plot_simulation_results_2d.py')
        for output_filename in output_filenames:
            assert Path(output_filename).exists() == True
            os.system('rm '+output_filename)

    def test_task_8_part_3(self):

        os.chdir(Path(cwd))
        os.chdir(Path('tasks/task_8'))
        output_filename = 'TBR_vs_thickness_vs_enrichment_fraction.html'
        os.system('rm '+output_filename)
        os.system('python plot_simulation_results_3d.py')
        assert Path(output_filename).exists() == True
        os.system('rm '+output_filename)
        os.system('rm outputs/*.json')
        os.system('rmdir outputs')

    def test_task_8_part_4(self):

        os.chdir(Path(cwd))
        os.chdir(Path('tasks/task_8'))
        os.system('rm outputs/*.json')
        os.system('rmdir outputs')
        os.system('python 1_simulate_with_halton_sample.py')
        assert Path('outputs').exists() == True
        assert len(os.listdir('outputs')) != 0



class test_task_9(unittest.TestCase):
    def test_task_9_part_1(self):

        os.chdir(Path(cwd))
        os.chdir(Path('tasks/task_9'))
        output_filenames = ['simulation_results.json', 'output.gif']
        for output_filename in output_filenames:
            os.system('rm '+output_filename)
        os.system('python lithium_enrichment_optimisation.py')
        for output_filename in output_filenames:
            assert Path(output_filename).exists() == True
            os.system('rm '+output_filename)

    def test_task_9_part_2(self):
        # lithium_enrichment_and_thickness_optimisation.py
        # test output (output not actually working yet)
        pass



class test_task_10(unittest.TestCase):
    def test_task_10_part_1(self):

        os.chdir(Path(cwd))
        os.chdir(Path('tasks/task_10'))
        output_filename = 'cad_simulation_results.json'
        os.system('rm '+output_filename)
        os.system('python example_CAD_simulation.py')
        assert Path(output_filename).exists() == True
        os.system('rm '+output_filename)
