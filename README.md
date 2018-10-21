Example of Jenkins pipeline
============================

Example taken is for Python.

First we create a Docker image that will contain anything that's necessary for testing
*This is well in a non-scaled environment where you'd expect to have a single build node, when you want to scale, make a generic image that will be stored in your Docker registry and pulled instead of built* 
 
Then, inside this image we run all that's needed to validate the code.

Finally, package everything that's needed to run the app into the production image that's finally going to be deployed.
*Ideally at this stage we should also make white-box tests on the generated image to ensure that between testing and packaging, everything went fine, but that's a matter of safety vs trust*
