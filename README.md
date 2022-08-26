# Parte 1 - Spark Streaming contabilizando palavras de entrada via socket

Igor Batista Paiva - 18/0018278

## Sobre

Para executar será necessário ter instalado o `docker` e `docker-compose`.

## Configuração

Para instalar todas as dependências e criar todos os elementos necessários utilize o comando abaixo:

```
bash setup.sh
```

## Como executar

Após ter rodado o *setup* com sucesso para iniciar novamente só é necessário subir os containers e seguir os demais passos.

### Iniciar os containers

```
docker-compose up

# se prefirir utilize a flag -d para subir em modo detach
```

Quando aparecer algo semelhante ao exemplo abaixo, siga para o próximo passo

```
Creating spark_test_master_1 ... done
Creating spark_test_socket_1 ... done
Creating spark_test_spark-worker-2_1 ... done
Creating spark_test_spark-worker-1_1 ... done
Creating spark_test_submit_1         ... done
Attaching to spark_test_socket_1, spark_test_master_1, spark_test_spark-worker-1_1, spark_test_spark-worker-2_1, spark_test_submit_1
socket_1          | Server listening in localhost:9999...
socket_1          |
```

### Versão local

Entre no container:

```
docker exec -it spark_socket_submit_1 bash
```

Para submeter o problema:

```
# pode ser qualquer arquivo

./spark-3.1.3-bin-hadoop3.2/bin/spark-submit local.py > results_local.txt
```

### Versão cluster

#### Iniciar o master

```
docker exec -it spark_socket_master_1 bash spark-3.1.3-bin-hadoop3.2/sbin/start-master.sh
```

#### Iniciar os workers

```
docker exec -it spark_socket_spark-worker-1_1 bash spark-3.1.3-bin-hadoop3.2/sbin/start-worker.sh -m 1G -c 1 spark://master:7077 && docker exec -it spark_socket_spark-worker-2_1 bash spark-3.1.3-bin-hadoop3.2/sbin/start-worker.sh -m 1G -c 1 spark://master:7077
```

#### Submeter o problema

Em um novo terminal entre no container do submit:

```
docker exec -it spark_socket_submit_1 bash
```

Para submeter o problema:

```
# pode ser qualquer arquivo

./spark-3.1.3-bin-hadoop3.2/bin/spark-submit cluster.py > results_cluster.txt
```

## Resultados

Os resultados da contagem vai estar dentro do arquivo informado no passo anterior.

O formato é o seguinte:

```
-------------------------------------------
Time: 2022-08-21 21:57:56
-------------------------------------------
('And', 1)
('poinciana—had', 1)
('Sue', 1)
('an', 1)
('American', 1)
('would', 1)
('cross', 1)
('"Plan', 1)
('of', 1)
('Yoo,', 1)
('president', 1)
('the', 2)
('15', 1)
('persons', 1)

-------------------------------------------
Time: 2022-08-21 21:57:56
-------------------------------------------
14                                             # TOTAL DE PALAVRAS
```
