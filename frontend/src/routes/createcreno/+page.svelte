<script lang="ts">
    import Creno from "$lib/compo/creno.svelte";
    import type { Creneau } from "$lib/types";
    import { creneaux, addCreneau, removeCreneau } from "$lib/stores/creneaux";

    function addCreneax(){
        addCreneau({ id: 1, nom: "Créneau 1", start: "2023-10-01T08:00:00", duration: 60 });
    }

</script>


<h1>Créer les créneaux</h1>
<button on:click={addCreneax}>+</button>

<Creno></Creno>




<style lang="scss">

</style>