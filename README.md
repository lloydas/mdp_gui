# mdp_gui

# Only setup neccesary is to install the neccesary libraries, which are in requirements.txt, run:
pip install -r requirements.txt

# to run (the old) gui:
python3 main.py

# to run the new gui:
	cd into directory "new_gui_lewei"
	python main.py <dirname>

# Make Sure:
	the <dirname> is at the same level as main.py
	there are only image files in <dirname>

# Functions:
	on MENU page:
	display the menu treeview for <dirname>
	For a non-h5 file, 
		display the filename
	For a h5 file, 
		display a dropdown images of the file
		display a dropdown rasters of each image

	when a non-h5 image file is chosen, or a h5 file + image + raster is chosen,
		display the image on menu page


	on INFO page:
		display the pixel information of the image as a histogram
		refresh the histogram with input parameters when click on "update" button
		