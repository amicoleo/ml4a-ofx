## Fast Reverse Image Search

------
### Using it for new app with a custom data-set

#### TRAIN

##### Collect and organise images

- Download images online

    Pinterest + Google Chrome Addon [Gallerify](https://chrome.google.com/webstore/detail/gallerify-powerful-image/hlmlhalegjopepcnfbnphmpobjkjhdgk?hl=en) is a good combination.

    Might want to look at [this](https://chrome.google.com/webstore/detail/downloads-overwrite-exist/fkomnceojfhfkgjgcijfahmgeljomcfk?hl=en) addon as well, for avoiding to have duplicate images (which happens for instance on Pinterest)

    Put all images in a folder.

- Organize images in folders val, train, test

  Use the script `organizeImages.py`

    ```
    python organizeImages.py FOLDER_WITH_IMAGES
    ```

##### Training in the app

Run the current example

- Analyze images (pass it the folder)
- Save

#### USE

Uncomment the lines below (in ofApp::setup() function )

```
baseDir = ofToDataPath(IMAGE_FOLDER);
load(ofToDataPath(DAT_FILE_PATH), baseDir);
runKDTree();

```

** IMPORTANT: Loading the model will break the training function (an issue with paths), so either use one or the other**

------


[A complete guide to this application can be found here](http://ml4a.github.io/guides/ReverseImageSearchFast/)

This app requires:
 - [ofxCcv](https://github.com/kylemcdonald/ofxCcv)
 - [ofxLearn](https://github.com/genekogan/ofxLearn)
 - [ofxKDTree](https://github.com/genekogan/ofxKDTree)

Fast reverse image search on a live image, including webcam, video, or saved image. For same thing, but able to use a screengrab as an input, see [ReverseImageSearchLive](https://github.com/ml4a/ml4a-ofx/tree/master/apps/ReverseImageSearchLive).

The app collects images from a directory (recursively) and extracts a feature vector from each one, using a convolutional neural net. It then computes a principal component analysis on the entire feature vector set (to reduce the dimensionality) and saves all of it to file. At run-time, the PCA-projected feature vectors are embedded into a [k-d tree](https://en.wikipedia.org/wiki/K-d_tree) for fast nearest neighbor search. A live input image is analyzed in the same fashion (extracted with a convnet and projected to the same PCA-reduced space), and `k` nearest neighbors are fetched from the k-d tree and loaded on disk.

Better instructions how to use this soon. Also, a model which has been trained on [MS-Coco](http://mscoco.org/) (~145,000 images) will be uploaded and made available shortly.

For a screengrab of this being done live, [see here](https://twitter.com/ml4a_/status/835874470606798848).
