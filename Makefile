DEMO_FILE=./interactive_models.py

lock:
	poetry lock

install-deps:
	poetry install

shell:
ifeq (,$(shell which ipython))
	python -i $(DEMO_FILE)
else
	ipython -i $(DEMO_FILE)
endif