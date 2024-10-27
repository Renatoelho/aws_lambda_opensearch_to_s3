

# Deploy de uma Aplicação AWS Lambda

+ Clonando o projeto

```bash
git clone https://github.com/Renatoelho/aws_lambda_opensearch_to_s3.git aws_lambda_opensearch_to_s3
```

```bash
cd aws_lambda_opensearch_to_s3/
```

+ Crie o arquivo ```.env``` com o seguinte conteúdo:

```text
OPENSEARCH_HOST="localhost"
OPENSEARCH_PORT="9200"
OPENSEARCH_PASSWD="<Senha de acesso ao Elasticsearxh>"
OPENSEARCH_USER="elastic"
MINIO_ROOT_USER="admin"
MINIO_ROOT_PASSWORD="<Senha de acesso ao MinIO>"
INDEX_LIST="index-tes1,index-tes2,index-tes3"
AWS_ACCESS_KEY="<Access Key Minio ou S3>" # Atualizar aqui depois de subir o MinIO
AWS_SECRET_KEY="<Secret Key Minio ou S3>" # Atualizar aqui depois de subir o MinIO
AWS_REGION_NAME="sa-east-1"
AWS_ENDPOINT="http://localhost:9000"
AWS_BUCKET="lambda"
AWS_BUCKET_KEY="dir/test/output.txt"
```

+ Ative essas variáveis no ambiente local e no console da AWS Lambda.

```bash
export OPENSEARCH_HOST="localhost" && \
export OPENSEARCH_PORT="9200" && \
export OPENSEARCH_PASSWD="<Senha de acesso ao Elasticsearxh>" && \
export OPENSEARCH_USER="elastic" && \
export MINIO_ROOT_USER="admin" && \
export MINIO_ROOT_PASSWORD="<Senha de acesso ao MinIO>" && \
export INDEX_LIST="index-tes1,index-tes2,index-tes3" && \
export AWS_ACCESS_KEY="<Access Key Minio ou S3>"  && \
export AWS_SECRET_KEY="<Secret Key Minio ou S3>"  && \
export AWS_REGION_NAME="sa-east-1" && \
export AWS_ENDPOINT="http://localhost:9000" && \
export AWS_BUCKET="lambda" && \
export AWS_BUCKET_KEY="dir/test/output.txt"
```

+ Ativando os serviços via Docker Compose

```bash
docker compose --env-file ./.env -p lambda -f docker-compose.yaml up -d
```

+ Acessando o MinIO

[http://localhost:9001/login](http://localhost:9001/login)

Usuário e senha estão no arquivo [./.env](./.env)

+ Configuração do Ambiente Python Local

```bash
python3.8 -m venv .venv
```

```bash
source .venv/bin/activate
```

```bash
pip install -U pip setuptools wheel --no-cache-dir && pip install -r requirements.txt --no-cache-dir
```

### Deploy AWS Lambda Function

```bash
cd aws_lambda_opensearch_to_s3/make/
```

```bash
sh make_lambda.sh
```

Arquivos em ```./make/lambda/lambda_function.zip``` e ```./make/lambda/layer_dependencies.zip``` prontos para ser importados no console AWS Lambda. Acesse o diretório dos arquivo [Aqui...](./make/).