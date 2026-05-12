
## Starting with OpenCL on Parallella Board ##

Note: All next steps should be done on Parallella Board.

STDCL® is a portable API for targeting compute offload accelertors and co-processors. STDCL is designed in a style inspired by familiar and traditional UNIX APIs for C programming. The implementation of STDCL leverages OpenCL™ to provide broad portability across modern accelerator and co-processor architectures.

STDCL provides the following features and support:

- Default compute contexts.

- Dynamic loader for compute-offload programs.

- Distributed memory management.

- Compute offload kernel execution.

- Synchronization.

More info: [http://www.browndeertechnology.com/coprthr_stdcl.htm](http://www.browndeertechnology.com/coprthr_stdcl.htm)!.

### Create folder ###

Go to the projects folder with "cd", or create it with "mkdir".

Into the projects folder:

Create a folder:

```
$ mkdir matvecmult
```

### Host code ###

Create the file "matvecmult_host.c":

```
$ sudo nano matvecmult_host.c
```

and write:

```
/* matvecmult_host.c */
    
#include <<x>stdio.h<x>>
#include <<x>stdlib.h<x>>
#include <<x>stdcl.h<x>>
    
inline int parity( int x ) { return ( (x%2)? +1 : -1 ); }
    
int main()
{
    int i,j;
    unsigned int n = 1024;
    
    /* allocate device-shareable memory */
    float* aa = (float*)clmalloc(stdacc,n*n*sizeof(float),0);
    float* b = (float*)clmalloc(stdacc,n*sizeof(float),0);
    float* c = (float*)clmalloc(stdacc,n*sizeof(float),0);
    
    /* initialize matrix aa[] and vector b[], and zero result vector c[] */
    for(i=0; i <<x> n; i++) for(j=0; j <<x> n; j++) aa[i*n+j] = (1.0/n/n)*i*j*parity(i*j);
    for(i=0; i <<x> n; i++) b[i] = (1.0/n)*i*parity(i);
    for(i=0; i <<x> n; i++) c[i] = 0.0f;
    
    /* sync data with device memory */
    clmsync(stdacc,0,aa,CL_MEM_DEVICE|CL_EVENT_NOWAIT);
    clmsync(stdacc,0,b,CL_MEM_DEVICE|CL_EVENT_NOWAIT);
    clmsync(stdacc,0,c,CL_MEM_DEVICE|CL_EVENT_NOWAIT);
    
    /* perform calculation */
    clndrange_t ndr = clndrange_init1d( 0, n, 16 );
    clexec(stdacc,0,&ndr,matvecmult_kern,n,aa,b,c);
    
    /* sync data with host memory */
    clmsync(stdacc,0,c,CL_MEM_HOST|CL_EVENT_NOWAIT);
    
    /* block until co-processor is done */
    clwait(stdacc,0,CL_ALL_EVENT);
    
    for(i=0; i <<x> n; i++) printf("%d %f %f\n",i,b[i],c[i]);
    
    clfree(aa);
    clfree(b);
    clfree(c);
}
```

Then save and exit.

### Kernel code ###

Create the file "matvecmult_kern.cl":

```
$ sudo nano matvecmult_kern.cl
```

and write:

```
/* matvecmult_kern.cl */
     
#include <<x>stdcl.h<x>>
      
void matvecmult_kern( unsigned int n, float* aa, float* b, float* c )
{
    int i,j;
     
    i = get_global_id(0);
     
    float tmp = 0.0f;
    for(j=0; j <<x> n; j++) tmp += aa[i*n+j] * b[j];
    c[i] = tmp;
}
```

Then save and exit.

### Program Compilation ###

Using the COPRTHR clcc compiler tools, building the program is easy and follows a standard compilation
model. The kernel code is first compiled using clcc and then the host program can be compiled with the
kernel code being directly linked to create a single executable program.

```
$ clcc -k -c matvecmult_kern.cl
```

```
$ gcc -o matvecmult.x matvecmult_host.c matvecmult_kern.o -I/usr/local/browndeer/include \
-L/usr/local/browndeer/lib -lstdcl -locl
```

We can verify that the kernel code is linked in using the clnm command:

```
$ clnm matvecmult.x
```

The last command should shows:

```
clnm: 'matvecmult_kern.c' bin [coprthr:ARMv7]
clnm: 'matvecmult_kern.c' bin [coprthr:E16G Needham]
clnm: 'matvecmult_kern.c' ksym matvecmult_kern
clnm: 'matvecmult_kern.c' src [<<x>generic<x>>]
```

### Run ###

We can then run the program that offloads the parallel computation to the Epiphany co-processor:

```
$ ./matvecmult.x
```

### Resources ###

-[http://dennis7dns.github.io/ParallellaPlatform/documentation/app_note_programming_parallella_using_stdcl.pdf](http://dennis7dns.github.io/ParallellaPlatform/documentation/app_note_programming_parallella_using_stdcl.pdf)!.

