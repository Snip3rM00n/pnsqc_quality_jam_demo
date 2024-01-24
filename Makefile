DEMO_FILE=./integration_example.py

lock:
	poetry lock

install-deps:
	poetry install

shell:
ifeq (,$(shell which ipython))
	python -i $(DEMO_FILE)
else
	ipython -i ./integration_example.py
endif