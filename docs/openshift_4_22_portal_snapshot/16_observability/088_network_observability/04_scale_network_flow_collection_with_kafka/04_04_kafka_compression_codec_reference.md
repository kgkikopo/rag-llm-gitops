# 4.4. Kafka compression codec reference

Compare Kafka compression codecs to choose the optimal algorithm for your environment. 

This reference applies to compression configured in both `spec.kafka.compression` for flow collection and `spec.exporters` for flow export. 

Table 4.1. Kafka compression codec comparisonCodec| Compression ratio| CPU cost (producer)| Decompression cost| Notes  
---|---|---|---|---  
`none` |  1x  |  N/A  |  N/A  |  No overhead. Use when CPU is the bottleneck.   
`lz4` |  2:1 to 3:1  |  Very low  |  Very low  |  **Recommended default.** Best latency-to-compression ratio trade-off.   
`snappy` |  2:1 to 3:1  |  Very low  |  Very low  |  Similar to `lz4`, with a slightly lower compression ratio.   
`zstd` |  3:1 to 5:1  |  Moderate  |  Low  |  Higher compression ratio. Good for high-throughput clusters.   
`gzip` |  3:1 to 5:1  |  High  |  Moderate  |  Maximum compression ratio but incurs a significant CPU cost.   
Show more

Note

The compression ratios and CPU cost estimates are approximate values derived from upstream benchmarks, not from Network Observability-specific measurements. Actual results vary depending on flow record characteristics and batch sizes.
