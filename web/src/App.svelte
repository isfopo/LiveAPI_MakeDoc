<script>
  import { onMount } from "svelte";

  let versions = [];

  onMount(async () => {
    try {
      const response = await fetch("/versions.json");
      if (response.ok) {
        versions = await response.json();
      } else {
        console.error("Failed to fetch versions.json:", response.statusText);
      }
    } catch (error) {
      console.error("Error fetching versions.json:", error);
    }
  });
</script>

<main>
  <h1>Available Versions</h1>
  <ul>
    {#each versions as version}
      <li><a href="{version}/Live.xml">Live Version {version}</a></li>
    {/each}
  </ul>
</main>

<style>
  main {
    padding: 1rem;
    font-family: Arial, sans-serif;
  }

  h1 {
    color: #333;
  }

  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    background: #f9f9f9;
    margin: 0.5rem 0;
    padding: 0.5rem;
    border-radius: 4px;
  }
</style>
