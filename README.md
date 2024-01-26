

 # Efficient Row-Level Lineage Leveraging Predicate Pushdown

 Row-level lineage explains what input rows produce an output row through a workflow, having many applications like data debugging, auditing, data integration, etc. 
In this repo, we introduce PredTrace, a lineage tracking system that achieves easy adaptation, low runtime overhead, efficient lineage querying, and high query/pipeline coverage. It achieves this by leveraging predicate pushdown: pushing a row-selection predicate that describes the target output down to source tables, and selects the lineage by running the pushed predicate.

We offer two options in PredTrace: one option slightly alters the original query/pipeline by saving intermediate results and returns the precise lineage; and another version without using intermediate results but may return a superset.


## Prerequisites
To install the package and prepare for use, run:
<pre><code>git clone https://github.com/PredTrace/predtrace_pipeline.git

pip install -r requirements.txt
</code></pre>

The following python packages are required to run PredTrace and z3.

## Demo

```bash
$ cd test/pipeline/
$ python3 evaluate_linage.py NB_8392403/
```

It will run the pipeline id NB_8392403 and show the lineage result for PredTrace and baseline as well as their runtime.

In this pipeline, all source tables return 1 row as the lineage row (exact lineage), with no requirement to save intermediate results.

To obtain the entire set of data science pipelines, please find: https://github.com/PredTrace/pipeline_code/blob/master/notebook_links.csv

For saving intermediate results and returning a lineage superset, check the example in https://github.com/PredTrace/predtrace_sql.
