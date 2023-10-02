<script lang="ts">
  import constants from '$lib/constants';
  import Cookies from 'js-cookie';

  async function test() {
    const req = await fetch(`${constants.API_URL}test/?token=${encodeURIComponent("eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..M7r-1r0alwPVP-nk.H0ysk__08awvj3DV09zw1572ZLCXJ65CQaxTBUf17bv60WWx-bhlzhsAVwpP--41AKQ-AO0RLH-AwtTrE7RbEHOKQbl9mXHGtVCJXFivtIey_M-DsaEr5C2Y1H1PhmSMBwS7Rh17qQBkPdmdUyY.baPBdP3VhoNd2G6kTs4FJA")}`, {
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