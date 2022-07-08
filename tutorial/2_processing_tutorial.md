Don't use XDS!! Instead go [here](https://docs.google.com/document/d/12xUN9CjI-50afmi3HdK_QFJuVoU7rYkB7QkXr72WC7s/edit#heading=h.cmfixdmu3t8g)

~~## Processing CCBXRAY data with XDS

~~### An XDS crash course

~~1. Download XDS [here](https://xds.mr.mpg.de/html_doc/downloading.html).  
~~     - As mentioned on the download page, you will need to add the directory containing the XDS executables to your `PATH`.  
~~     - Also, if you get an error, be sure you didn't forget about `xattr -dr com.apple.quarantine full_path_name_to/directory-containing-XDS/*`.  
~~
~~2. Craft an appropriate `XDS.INP` input file (follow the instructions below)
~~3. Run `xds` by simply typing `xds` into the terminal in the directory containing your `XDS.INP` file.
~~4. Use the output file `XDS_ASCII.HKL` for the next step in your data processing pipeline (aimless, or whatever) 
~~
~~### Making an `XDS.INP` file
~~
~~The [example `XDS.INP` file](/examples/XDS.INP) in this repo is a good starting point. You'll additionally want to:

~~Use the script in this repo to create an appropriate lower chunk of the file, and copy paste that in. You'll find the appropriate numbers in your `.exp` file
Change the image file names as appropriate
If known, add the space group and unit cell

~~***To Do: flesh out these instructions!!***
