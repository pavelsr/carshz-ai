# Dockerfiles для утилит

TODO: попробовать минимизировать размер образов за счет python-alpine

```
FROM python:3.9-alpine
RUN apk add build-base gcompat libstdc++ musl llvm17 git
```


У bgremover first run может занимать около 1.5 мин
