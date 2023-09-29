<script lang="ts">
    import type { Creneau } from "$lib/types";
    import { creneaux, addCreneau, removeCreneau } from "$lib/stores/creneaux";
    
</script>

{#each $creneaux as creno (creno.id)}
<div class="container">
  <input type="text" bind:value={creno.nom} placeholder="nom créneau">
  <input type="datetime-local" bind:value={creno.start} name="start">
  <select bind:value={creno.duration} name="duration">
    <option value="0">30</option>
    <option value="1">60</option>
    <option value="2">90</option>
    <option value="3">120</option>
  </select>
  
  <div class="buttons">
    <button on:click={() => console.log("Save", creno)}><i class="fa-solid fa-check"></i></button>
    <button on:click={() => console.log("Delete", creno)}><i class="fa-solid fa-dumpster"></i></button>
  </div>
</div>
{/each}

<style lang="scss">
.container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    border : 1px solid black;
    border-radius: 20px;
}

.buttons{
    display: flex;
    flex-direction: row;
}
</style>