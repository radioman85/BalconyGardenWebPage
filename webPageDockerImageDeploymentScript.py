import subprocess

# Build the Docker image
subprocess.run(['docker-compose', '-f', 'webPageDockerImageBuilder.yml', 'build', 'greenhouse-web-app'], check=True)

# Tag the Docker image
subprocess.run(['docker', 'tag', 'balconygardenwebpage-greenhouse-web-app', 'radioman85/greenhouse-web-app'], check=True)

# Push the Docker image to Docker Hub
subprocess.run(['docker', 'push', 'radioman85/greenhouse-web-app'], check=True)