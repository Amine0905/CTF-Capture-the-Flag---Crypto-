#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <string.h>

#include "md5.h"
#include "coll.h"

// Fonction pour afficher l'empreinte MD5
static void print_md5(unsigned char digest[16]) {
  int i;

  for (i = 0; i < 16; i++)
    printf ("%02x", digest[i]);
}

// Fonction pour calculer l'empreinte MD5 d'un fichier
static void md_file(char *filename) {
  FILE *file;
  MD5_CTX context;
  int len, i;
  unsigned char buffer[1024], digest[16];

  if ((file = fopen (filename, "rb")) == NULL)
    printf ("%s ne peut pas être ouvert\n", filename);
  else {
    MD5Init (&context);
    while ((len = fread (buffer, 1, 1024, file))) 
      MD5Update (&context, buffer, len);
    MD5Final (digest, &context);

    fclose (file);

    printf ("MD5 (%s) = ", filename);
    print_md5(digest);
    printf ("\n");
  }
}

int main(int argc, char **argv) {
  FILE *prefix_file, *output_file;
  MD5_CTX context;
  uint32_t msg1_block0[16], msg1_block1[16], msg2_block0[16], msg2_block1[16];
  int len, i;
  unsigned char buffer[1024], digest[16];

  // Vérification des arguments de la ligne de commande
  if (argc != 4) {
    printf("usage : %s [fichier préfixe] [sortie 1] [sortie 2]\n\n", argv[0]);
    printf("Ceci génère deux fichiers, [sortie 1] et [sortie 2], tels que :\n");
    printf("  #cat [fichier préfixe] [sortie 1] | md5sum\n");
    printf("  #cat [fichier préfixe] [sortie 2] | md5sum\n");
    printf("sont égaux. La taille du [fichier préfixe] doit être un multiple de 64.\n\n");
    exit(0);
  }

  // Ouverture du fichier préfixe
  prefix_file = fopen(argv[1], "rb");
  if (prefix_file == NULL) {
    fprintf (stderr, "%s ne peut pas être ouvert\n", argv[1]);
    exit(1);
  }

  // Initialisation du contexte MD5 et lecture du fichier préfixe
  MD5Init(&context);
  while ((len = fread(buffer, 1, 1024, prefix_file))) {
    MD5Update(&context, buffer, len);
    if ((len % 64) != 0) {
      fprintf (stderr, "La taille de %s n'est pas un multiple de 512 bits\n", argv[1]);
      exit(1);
    }
  }
  fclose(prefix_file);

  // Recherche de la collision
  find_collision(context.state, msg1_block0, msg1_block1, msg2_block0, msg2_block1, 1);

  // Écriture de la première sortie
  output_file = fopen(argv[2], "wb");
  if (output_file == NULL) {
    fprintf (stderr, "%s ne peut pas être ouvert\n", argv[2]);
    exit(1);
  }
  fwrite(msg1_block0, 1, 64, output_file);
  fwrite(msg1_block1, 1, 64, output_file);
  fclose(output_file);

  // Écriture de la deuxième sortie
  output_file = fopen(argv[3], "wb");
  if (output_file == NULL) {
    fprintf (stderr, "%s ne peut pas être ouvert\n", argv[3]);
    exit(1);
  }
  fwrite(msg2_block0, 1, 64, output_file);
  fwrite(msg2_block1, 1, 64, output_file);
  fclose(output_file);

  return 0;
}
