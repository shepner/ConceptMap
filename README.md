# ConceptMap

index.html
* This is the output presentation script

tbd.py
* generate the json file(s) to be parsed

tbd2.py
* capture and store the data
* 1 json file per node
* use dir structures to create hierarchy
  * the structure should be based on the size of the dir.  If it gets too big, break it up
  * use a dir per node if there are files to go with the json file
  * dir structure example:  for 6cdc1aef-e1c5-42ca-a845-7536323a4c9b
    * ~/e1/42/a8/75/6cdc1aef-e1c5-42ca-a845-7536323a4c9b.json

index.html
which points to whatever.png and some/dir/file.txt

---

Think of the overall dir structure as a book (more or less) with Contents, Index, and Content.  Each node is effectively a Chapter which can have its own recursive dir structure within.

general structure
* top level
  * ~/root.json
  * ~/index.html
    * this is the table of contents/index
    * phase1:  create directly from the node level .json files
  * ~/tags.json
    * this is the central list of all tags but can be generated from the tags.json files within the dir structure
  * ~/dirs.json
    * this is the central list of all dirs but can be generated from the dirs.json files within the dir structure
  * ~/urls.json
    * this is the central list of all urls but can be generated from the urls.json files within the dir structure

* top of the node
  * ~/68/47/94/69/9b699b08-684f-47de-940f-69b8767b3416.json
    * This is the table of contents of the "chapter" so it is a node pointing to the content
    * Could be fully recovered from the content

* make the contents of the node presentable
  * ~/68/47/94/69/9b699b08-684f-47de-940f-69b8767b3416/index.html
    * used to display the contents of the dir structure

* source metadata
  * ~/68/47/94/69/9b699b08-684f-47de-940f-69b8767b3416/url.json
    * file for bookmark URLs etc
  * ~/68/47/94/69/9b699b08-684f-47de-940f-69b8767b3416/tags.json
    * file containing all the tags
  * ~/68/47/94/69/9b699b08-684f-47de-940f-69b8767b3416/dirs.json
    * metadata about the directories
    * Would also be used for generating index.html

* example captured website
  * ~/df/11/ab/ce/0cf95454-bf08-11e7-abc4-cec278b6b50a.json
  * ~/df/11/ab/ce/0cf95454-bf08-11e7-abc4-cec278b6b50a/tags.json
  * ~/df/11/ab/ce/0cf95454-bf08-11e7-abc4-cec278b6b50a/dirs.json
  * ~/df/11/ab/ce/0cf95454-bf08-11e7-abc4-cec278b6b50a/urls.json
  * ~/df/11/ab/ce/0cf95454-bf08-11e7-abc4-cec278b6b50a/index.html
    * auto-generated and points to `whatever.html` to redirect
  * ~/df/11/ab/ce/0cf95454-bf08-11e7-abc4-cec278b6b50a/whatever.html
    * downloaded content
  * ~/df/11/ab/ce/0cf95454-bf08-11e7-abc4-cec278b6b50a/someimage.png
    * downloaded content
  * ~/df/11/ab/ce/0cf95454-bf08-11e7-abc4-cec278b6b50a/somefile.pdf
    * downloaded content
  * ~/df/11/ab/ce/0cf95454-bf08-11e7-abc4-cec278b6b50a/etc.html
    * downloaded content

* another example captured webpage
  * ~/68/47/94/69/9b699b08-684f-47de-940f-69b8767b3416/c6bdbb82-42a5-440d-84e2-aba3b75ddcbf/index.html
  * ~/68/47/94/69/9b699b08-684f-47de-940f-69b8767b3416/c6bdbb82-42a5-440d-84e2-aba3b75ddcbf/etc.png

* saved files/directories
  * ~/68/47/94/69/9b699b08-684f-47de-940f-69b8767b3416.json
    * a ref to `9011a66a-3f60-4c17-80c5-b3d078b4964e.json` would indicate the ref node is a child the current node
    * a reference to `9011a66a-3f60-4c17-80c5-b3d078b4964e/vmware/license.txt` would just be a link to that file
    * this node could contain tags like "license", "documentation", "VMware", etc
    * any external file ref MUST start with the UUID
  * ~/68/47/94/69/9b699b08-684f-47de-940f-69b8767b3416/<some additional crap goes here if desired>
    * the subdir is exclusively user content and out of scope for the tool (unless explicitly linked otherwise?)
  * ~/3f/4c/80/b3/9011a66a-3f60-4c17-80c5-b3d078b4964e.json
    * this really can only give tags and such for the dir tree below as a whole
    * The "file" key value should only primary item (file or subdir) contained within
        * so, the "file" key value should only contain "vmware" as it is the top level of the dir.
        * this could also be the index.html if it was a captured webpage.
        * it is permissible to have multiple if desired.
    * Each sub-dir or file below that level should have its own separate node (if desired).  ie the example of "~/68/47/94/69/9b699b08-684f-47de-940f-69b8767b3416.json' above.
  * ~/3f/4c/80/b3/9011a66a-3f60-4c17-80c5-b3d078b4964e/index.html
    * in this case, we generated this file
  * ~/3f/4c/80/b3/9011a66a-3f60-4c17-80c5-b3d078b4964e/vmware/somerandomfile
  * ~/3f/4c/80/b3/9011a66a-3f60-4c17-80c5-b3d078b4964e/vmware/ESXi/3.0/installername.exe
  * ~/3f/4c/80/b3/9011a66a-3f60-4c17-80c5-b3d078b4964e/vmware/ESXi/3.0/license.txt
  * ~/3f/4c/80/b3/9011a66a-3f60-4c17-80c5-b3d078b4964e/vmware/ESXi/3.0/someotherinstaller.exe
  * ~/3f/4c/80/b3/9011a66a-3f60-4c17-80c5-b3d078b4964e/vmware/ESXi/4.5/...
  * ~/3f/4c/80/b3/9011a66a-3f60-4c17-80c5-b3d078b4964e/vmware/GSX/2/...
  
* another method of storing webpages
  * ~/68/47/94/69/9b699b08-684f-47de-940f-69b8767b3416/2ce6dade-9b26-49f9-b751-7f7a1e417a00.json
    * this could have a reference to 9b699b08-684f-47de-940f-69b8767b3416/9011a66a-3f60-4c17-80c5-b3d078b4964e/vmware/ESXi/3.0/installername.exe
  * ~/9b/49/b7/7f/2ce6dade-9b26-49f9-b751-7f7a1e417a00/8a87e840-6dff-467a-8628-a8a0bb92f838.html
  * ~/68/47/94/69/9b699b08-684f-47de-940f-69b8767b3416/2ce6dade-9b26-49f9-b751-7f7a1e417a00/831ef490-ab13-4b4c-8527-74b95be38502.html
  * ~/68/47/94/69/9b699b08-684f-47de-940f-69b8767b3416/2ce6dade-9b26-49f9-b751-7f7a1e417a00/7acfb803-4372-4e8f-9343-b6133cae847f.png
  * ~/68/47/94/69/9b699b08-684f-47de-940f-69b8767b3416/2ce6dade-9b26-49f9-b751-7f7a1e417a00/0604274b-4855-4f3a-a0a3-a0fb162e9871.pdf
  

file named should be based on the UUID of that object (ie 915c5d89-3056-4c66-a85d-fa87ee4ff198.json or e973170b-5812-4e0e-b33a-7c03d0a2cdee.png)

<img src="https://imgs.xkcd.com/comics/digital_resource_lifespan_2x.png" align="center" width="500" height="400">



[D3.js API documentation](https://github.com/d3/d3/blob/master/API.md)
