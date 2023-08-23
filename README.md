# Balcony Garden Web Page
This repositories containes the web page source files/project. It containes the development artefacts for a webpage (set up using visual studio) which is part of my IoT project (check out the main repository: [BalconyGarden](https://github.com/radioman85/BalconyGarden)). This webpage eventually allows me to connect and control the embedded system, which controlles (opening/closing) the window of my greenhouse.

![image](https://user-images.githubusercontent.com/25708993/236409648-ba06ff9e-786c-4ef6-b97f-f753d4bc3a1e.png)


# My Workflow
1. update/modified/complete/manipulate what ever you need to gain your purpose.
2. publish the web page
3. build a docker image
4. tag image
5. deploy the docker image to [Docker Hub](https://hub.docker.com/) (Be aware that you have to set up your own hub).

Restart the docker container, which is part of the cloud services described here: [BalconyGardenCloudServices](https://github.com/radioman85/BalconyGardenCloudServices)

For point 3 to 5 you can simply use the provides python script. Make sure you update the script adding the credentials of your own docker hub.

```
python webPageDockerImageDeploymentScript.py
```

### Step by Step deployment
Build docker image:
```
docker-compose -f webPageDockerImageBuilder.yml build greenhouse-web-app
```
Tag docker image:
```
docker tag balconygardenwebpage-greenhouse-web-app radioman85/greenhouse-web-app
```
Push to Docker Hub:
```
docker push radioman85/greenhouse-web-app
```


# Related Repositories
- Top Level Repo: [BalconyGarden](https://github.com/radioman85/BalconyGarden)
- Embedded System: [Greenhouse Embedded](https://github.com/radioman85/GreenhouseEmbedded)
- Cloud Services: [Balcony Garden Cloud Services](https://github.com/radioman85/BalconyGardenCloudServices)
