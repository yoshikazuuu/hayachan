from discord.ext import commands
from zipfile import ZipFile
import discord
import glob
import os

class Get(commands.Cog, name="Download"):
    """For Downloading listed files"""


    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def get(self, ctx: commands.Context, lab, week=None, problem=None):
        """
        Get the .pdf files for the desired problem

        Example: 
        `haya get BG75 3 A`
        `haya get BG75 5`
        `haya get BG75`
        `haya get all`
        """

       

        def get_all_file_paths(directory):
        
            # initializing empty file paths list
            file_paths = []
        
            # crawling through directory and subdirectories
            for root, directories, files in os.walk(directory):
                for filename in files:
                    # join the two strings in order to form the full filepath.
                    filepath = os.path.join(root, filename)
                    file_paths.append(filepath)
        
            # returning all file paths
            return file_paths            

        def bulking():
            # path to folder which needs to be zipped
            directory = './problems'
        
            # calling function to get all file paths in the directory
            file_paths = get_all_file_paths(directory)
            file_paths.sort()
        
            # # printing the list of all files to be zipped
            # for file_name in file_paths:
            #     print(file_name)
        
            # writing files to a zipfile
            with ZipFile('./zipped/problems-' + temp  +'.zip','w') as zip:
                print('Following files will be zipped:')
                # writing each file one by one
                # Counting if file exist or not
                global counter
                counter = False;
                for file in file_paths:
                    if lab != 'all':
                        if file.find(lab): 
                            print(file)
                            zip.write(file)
                            counter = True
                        else: continue
                    else:
                        print(file)
                        zip.write(file)
                        counter = True;
                        
                if counter:
                    print("file doesn't exists")
                    return

            print('All files zipped successfully!') 

        if lab == 'all':
            temp = lab
        elif lab and week:
            temp = lab.upper() + '-week-' + str(week.upper())    
        elif lab:
            temp = lab.upper()

        print(temp)

        if lab == 'all':
            print("all no temp")
            if os.path.exists('./zipped/problems-' + temp  +'.zip'):
                print("File exist!")
                await ctx.send("Uploading...")
                await ctx.send(file=discord.File('./zipped/problems-' + temp  +'.zip'))
            else:
                bulking()  
                if not counter:
                    await ctx.send("Uploading...")
                    await ctx.send(file=discord.File('./zipped/problems-' + temp  +'.zip'))
                else:
                    await ctx.send("File doesn't exist! Please, check it using `haya list`, nii-sama!")
        elif lab and week and problem:
            problem = problem.upper()
            lab = lab.upper()
            await ctx.send("Uploading...")
            file_path = glob.glob("./problems/*/" + lab + '-week-' + week + '-prob-' + problem + '.pdf')
            await ctx.send(file=discord.File(file_path[0]))
        elif lab and week:
            print("lab and week zip")
            if os.path.exists('./zipped/problems-' + temp  +'.zip'):
                print("File exist!")
                await ctx.send("Uploading...")
                await ctx.send(file=discord.File('./zipped/problems-' + temp  +'.zip'))
            else:
                bulking()  
                if not counter:
                    await ctx.send("Uploading...")
                    await ctx.send(file=discord.File('./problems/problems-' + temp  +'.zip'))
                else:
                    await ctx.send("File doesn't exist! Please, check it using `haya list`, nii-sama!")
        elif lab:
            print("lab zip")
            if os.path.exists('./zipped/problems-' + temp  +'.zip'):
                print("File exist!")
                await ctx.send("Uploading...")
                await ctx.send(file=discord.File('./zipped/problems-' + temp  +'.zip'))
            else:
                if not counter:
                    await ctx.send("Uploading...")
                    await ctx.send(file=discord.File('./zipped/problems-' + temp  +'.zip'))
                else:
                    await ctx.send("File doesn't exist! Please, check it using `haya list`, nii-sama!")

async def setup(bot: commands.Bot):
    await bot.add_cog(Get(bot))