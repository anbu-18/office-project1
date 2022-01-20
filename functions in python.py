def simple():
    print(" I am a function")

simple()


def gbp_to_usd(gbp):
    usd=gbp*1.5
    return usd

usd=gbp_to_usd(5)
print(usd)


#function parameters

def name(name):
    print(name)
name('anbu')

def names(*name):
    print(name)

names("anbu","mohan","bharath","giri")

