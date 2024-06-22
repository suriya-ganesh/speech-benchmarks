DATA_ASR_DIR = dataset_asr

# Download data for ASR
get-asr-data:
	@echo "Downloading data..."
	@mkdir -p $(DATA_ASR_DIR)
	@wget -O $(DATA_ASR_DIR)/ta_in_female.zip https://www.openslr.org/resources/65/ta_in_female.zip
	@unzip $(DATA_ASR_DIR)/ta_in_female.zip -d $(DATA_ASR_DIR)/ta_in
	@wget -O $(DATA_ASR_DIR)/mile_tamil_asr_corpus.tar.gz wget https://www.openslr.org/resources/127/mile_tamil_asr_corpus.tar.gz
	@tar -xvf $(DATA_ASR_DIR)/mile_tamil_asr_corpus.tar.gz -C $(DATA_ASR_DIR)

	@echo "Data downloaded."

