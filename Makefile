VERSION := v0.1.0-dev
IMAGE_NAME_BASE=chatgpt-prepackaged
IMAGE_BASE=simon3458/${IMAGE_NAME_BASE}

build:
	docker build . -t ${IMAGE_BASE}:${VERSION}

push:
	docker push ${IMAGE_BASE}:${VERSION}

