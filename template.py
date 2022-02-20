from collections import namedtuple

HeadPos = namedtuple('HeadPos', 'line apo eos')
HeadPosSlice = namedtuple('HeadPosSlice', 'line slice')
DetailPos = namedtuple('DetailPos', 'apo eos')
DetailPosSlice = namedtuple('DetailPosSlice', 'slice')


class ParserTemplate:
    def __init__(self):
        self.name = 'default'
        self.pname: HeadPos = HeadPos(1, 19, 80)
        self.papo: HeadPos = HeadPos(4, 79, 105)
        self.peos: HeadPos = HeadPos(4, 145, 146)
        self.pacc: DetailPos = DetailPos(1, 25)
        self.pper: DetailPos = DetailPos(27, 51)
        self.pxre: DetailPos = DetailPos(97, 112)
        self.ppis: DetailPos = DetailPos(113, 128)
        self.fpa: str = '54.00'
        self.fpa_exception: str = '54.00.9'
        self.omades: str = '1267'
        self.omades_negative: str = '7'

    @classmethod
    def load_from_file(cls, file_path):
        cls = ParserTemplate()
        with open(file_path, encoding='utf8') as fil:
            for line in fil.readlines():
                if len(line) < 4:
                    continue
                name_unstriped, tail = line.split('=')
                pars = tail.split()
                name = name_unstriped.strip()
                if name == 'name':
                    cls.name = pars[0]
                if name == 'pname':
                    cls.set_pname(int(pars[0]), int(pars[1]), int(pars[2]))
                    continue
                if name == 'papo':
                    cls.set_papo(int(pars[0]), int(pars[1]), int(pars[2]))
                    continue
                if name == 'peos':
                    cls.set_peos(int(pars[0]), int(pars[1]), int(pars[2]))
                    continue
                if name == 'pacc':
                    cls.set_pacc(int(pars[0]), int(pars[1]))
                    continue
                if name == 'pper':
                    cls.set_pper(int(pars[0]), int(pars[1]))
                    continue
                if name == 'pxre':
                    cls.set_pxre(int(pars[0]), int(pars[1]))
                    continue
                if name == 'pis':
                    cls.set_ppis(int(pars[0]), int(pars[1]))
                    continue
                if name == 'fpa':
                    cls.fpa = pars[0]
                    continue
                if name == 'fpa_exception':
                    cls.fpa_exception = pars[0]
                    continue
                if name == 'omades':
                    cls.omades = pars[0]
                    continue
                if name == 'omades_negative':
                    cls.omades_negative = pars[0]
                    continue
        return cls

    def save2file(self, file_path):
        txtlist = [
            f'name = {self.name}',
            f'pname = {self.pname.line} {self.pname.apo} {self.pname.eos}',
            f'papo = {self.papo.line} {self.papo.apo} {self.papo.eos}',
            f'peos = {self.peos.line} {self.peos.apo} {self.peos.eos}',
            f'pacc = {self.pacc.apo} {self.pacc.eos}',
            f'pper = {self.pper.apo} {self.pper.eos}',
            f'pxre = {self.pxre.apo} {self.pxre.eos}',
            f'ppis = {self.ppis.apo} {self.ppis.eos}',
            f'fpa = {self.fpa}',
            f'fpa_exception = {self.fpa_exception}',
            f'omades = {self.omades}',
            f'omades_negative = {self.omades_negative}',
        ]
        with open(file_path, 'w', encoding='utf8') as fil:
            fil.write('\n'.join(txtlist))

    def set_pname(self, line: int, apo: int, eos: int):
        self.pname = HeadPos(line, apo, eos)

    @property
    def pname_slice(self):
        return HeadPosSlice(self.pname.line, slice(self.pname.apo, self.pname.eos))

    def set_papo(self, line: int, apo: int, eos: int):
        self.papo = HeadPos(line, apo, eos)

    @property
    def papo_slice(self):
        return HeadPosSlice(self.papo.line, slice(self.papo.apo, self.papo.eos))

    def set_peos(self, line: int, apo: int, eos: int):
        self.peos = HeadPos(line, apo, eos)

    @property
    def peos_slice(self):
        return HeadPosSlice(self.peos.line, slice(self.peos.apo, self.peos.eos))

    def set_pacc(self, apo: int, eos: int):
        self.pacc = DetailPos(apo, eos)

    @property
    def pacc_slice(self):
        return DetailPosSlice(slice(self.pacc.apo, self.pacc.eos))

    def set_pper(self, apo: int, eos: int):
        self.pper = DetailPos(apo, eos)

    @property
    def pper_slice(self):
        return DetailPosSlice(slice(self.pper.apo, self.pper.eos))

    def set_pxre(self, apo: int, eos: int):
        self.pxre = DetailPos(apo, eos)

    @property
    def pxre_slice(self):
        return DetailPosSlice(slice(self.pxre.apo, self.pxre.eos))

    def set_ppis(self, apo: int, eos: int):
        self.pxre = DetailPos(apo, eos)

    @property
    def ppis_slice(self):
        return DetailPosSlice(slice(self.ppis.apo, self.ppis.eos))

    def __repr__(self):
        txt = (
            f'ParserTemplate('
            f"name='{self.name}',"
            f'pname={self.pname},'
            f'papo={self.papo},'
            f'peos={self.peos},'
            f'pacc={self.pacc},'
            f'pper={self.pper},'
            f'pxre={self.pxre},'
            f'ppis={self.ppis},'
            f"fpa='{self.fpa}',"
            f"fpa_exception='{self.fpa_exception}',"
            f"omades='{self.omades}',"
            f"omades_negative='{self.omades_negative}'"
            f')'
        )
        return txt


if __name__ == '__main__':
    pte = ParserTemplate()
    pte.name = 'singular'
    pte.save2file('singular.tml')
    fresh = ParserTemplate.load_from_file('singular.tml')
    print(fresh)
