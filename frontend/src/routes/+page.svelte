<script lang="ts">
  import constants from '$lib/constants';
  import Cookies from 'js-cookie';
  
  async function test() {
    const req = await fetch(`${constants.API_URL}test/?token=${encodeURIComponent("eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..EAMaWWl8_fTA9UfQ.bBsU20EfdpofAzjm_t0ziAtSaPrWOT9fjfIvh6GdrWZyFX81cWYSJ2bfVXoaFgBn_aiTbL3cKhjUD3Yut51OtO2qqN-He7_QZqYZSWwJYP1ayPNnWSuDdNSMSCiUmNMMcXvAthFrU9ulGQyKn9aQug.Rvf0akmeKPBdmjXn3d6k_A")}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${Cookies.get("next-auth.session-token")}`
      },
    });
    const res = await req.json();
   //console.log(Cookies.get("next-auth.session-token"));
  }
</script>

<h1>SvelteKit Auth Example</h1>
<p>
  This is an example site to demonstrate how to use <a
    href="https://kit.svelte.dev/">SvelteKit</a
  >
  with <a href="https://sveltekit.authjs.dev">SvelteKit Auth</a> for authentication.
</p>

<button on:click={test}>Logout</button>