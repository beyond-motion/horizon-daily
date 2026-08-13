---
layout: default
title: "Horizon Summary: 2026-08-13 (EN)"
date: 2026-08-13
lang: en
---

> From 5 items, 2 important content pieces were selected

---

**Technology News**
1. [DRAM Technique Exposes Hidden CPU Privileges from Negative Ring](#item-tech-news-1) ⭐️ 8.0/10
2. [City2Graph converts urban geospatial data into heterogeneous graphs for GNNs](#item-tech-news-2) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [DRAM Technique Exposes Hidden CPU Privileges from Negative Ring](https://github.com/xoreaxeaxeax/skitter-creek-bath-salts) ⭐️ 8.0/10

A hardware security researcher has released a DRAM-focused exploitation technique on GitHub under the repository name skitter-creek-bath-salts, with a Black Hat talk expected to accompany it. Community discussion identifies Christopher Domas as the researcher behind the work and notes that the technique can expose processor features hidden in &\#x27;negative ring&\#x27; territory. The README reportedly indicates the attack works on AMD Jaguar, a 2013 low-power architecture, while mentioning different memory-controller base addresses on Zen 3. That leaves uncertainty about how far the attack extends to newer CPUs. The release highlights the growing attack surface created by modern DRAM controllers and binary blob initialization.

hackernews · matt\_d · Aug 13, 14:17 · [Discussion](https://news.ycombinator.com/item?id=49286341)

**「Background」** DRAM scrambling is a hardware feature used by AMD processors to obfuscate the mapping between physical addresses and DRAM rows and columns. The released tool, skitter-creek-bath-salts, targets AMD Family 16h \(Jaguar\) and works by flipping a single configuration bit in the DRAM controller, redirecting physical addresses so that hidden CPU subsystems—such as the Platform Security Processor \(PSP\), C6 power state, microcode, and System Management Mode \(SMM\)—become accessible. This attack surface exists because DRAM initialization and scrambling rely on proprietary binary blobs and undocumented memory controller registers.

**「Impact」** On vulnerable AMD platforms, this technique could let ring-0 root access reach hidden processor features in negative-ring territory, expanding the impact of a system compromise.

**「Community Discussion」** Commenters are enthusiastic about Christopher Domas&\#x27;s upcoming Black Hat talk and some see the DRAM attack surface as unsurprising given the complexity of modern memory controllers. Others question which newer CPUs are actually affected, noting that the README only confirms AMD Jaguar while mentioning Zen 3 base-address differences.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/xoreaxeaxeax/skitter-creek-bath-salts">GitHub - xoreaxeaxeax/ skitter - creek - bath - salts : Unlocking...</a></li>
<li><a href="https://dzen.ru/b/an3nioa_N0hzeys8">Один бит в контроллере DRAM открывает всю память... | Дзен</a></li>

</ul>
</details>

**Tags**: `#hardware-security`, `#DRAM`, `#exploitation`, `#reverse-engineering`, `#systems`

---

<a id="item-tech-news-2"></a>
### [City2Graph converts urban geospatial data into heterogeneous graphs for GNNs](https://www.reddit.com/gallery/1vn8oya) ⭐️ 7.0/10

City2Graph is a newly released open-source Python library that turns geospatial urban data into analysis-ready heterogeneous graphs for spatial analysis, network analysis, and Graph Neural Networks as GeoAI, with a paper describing it now published. It supports morphology graphs from OpenStreetMap and Overture Maps, transportation graphs from GTFS and GBFS feeds loaded through DuckDB, mobility OD matrices and flow data, proximity and contiguity graph generators under multiple distance metrics, heterogeneous node/edge types with metapath-derived edges, and round-trip conversion between GeoDataFrames, NetworkX, rustworkx, and PyTorch Geometric Data/HeteroData while preserving geometries and attributes. The provided example demonstrates building a heterogeneous morphological graph from buildings and street segments and then converting it directly to PyTorch Geometric. The library aims to address why urban data is better represented as heterogeneous graphs rather than a single generic graph structure.

reddit · r/MachineLearning · Tough\_Ad\_6598 · Aug 13, 11:59 · [Discussion](https://www.reddit.com/r/MachineLearning/comments/1vn8oya/city2graph_a_python_library_for_heterogeneous/)

**「Background」** Urban data is often stored as flat geospatial tables or homogeneous graphs, which can obscure the different roles of buildings, streets, transit stops, and mobility flows. City2Graph is an open-source Python library that converts such data into heterogeneous graphs—where nodes and edges can have multiple distinct types—and provides direct conversion to PyTorch Geometric Data or HeteroData objects for graph neural network workflows. It supports sources like OpenStreetMap, Overture Maps, GTFS, and GBFS, making it a practical bridge between raw geospatial information and graph-based GeoAI models.

**「Impact」** City2Graph gives urban computing researchers and GeoAI developers a practical, low-friction bridge from common geospatial and mobility data sources to PyTorch Geometric, reducing the effort needed to build heterogeneous graph datasets for machine learning. The strong positive community reception suggests it may fill a real gap in the open-source geospatial graph tooling ecosystem.

**「Community discussion」** Commenters were enthusiastic, calling the idea &quot;pretty cool&quot; and describing it as &quot;the best library I&\#x27;ve seen in this year,&quot; with several saying they would try it or share it with collaborators. One user asked for an ELI5 explanation, indicating interest from less technical readers as well.

<details><summary>References</summary>
<ul>
<li><a href="https://livrepository.liverpool.ac.uk/3199917/">City 2 Graph : A Python library for Heterogeneous Graph Neural ...</a></li>

</ul>
</details>

**Tags**: `#geospatial`, `#graph-neural-networks`, `#urban-computing`, `#python`, `#open-source`

---