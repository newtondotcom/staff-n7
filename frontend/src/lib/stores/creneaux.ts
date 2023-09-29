import type { Creneau } from "$lib/types";
import { writable } from "svelte/store";

// Create a writable store and export its methods
export const creneaux = writable<Creneau[]>([]);

// You can optionally define some utility functions to interact with the store
export function addCreneau(creneau: Creneau) {
  creneaux.update((currentCreneaux) => [...currentCreneaux, creneau]);
}

export function removeCreneau(id: number) {
  creneaux.update((currentCreneaux) => currentCreneaux.filter((c) => c.id !== id));
}
